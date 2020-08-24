import time
import datetime
import MySQLdb
import discord

TERMINATE = False

db_pool = {}
db_pool_id = 0

def databaseConnect():
    conn_info = None

    conn_id_todelete = []

    global db_pool
    global db_pool_id

    # Iterate through open connections and find the currently active one.
    for pool_id in db_pool:
        conn_info_iter = db_pool.get(pool_id)

        if conn_info_iter['closed'] is True:
            if conn_info_iter['count'] <= 0:
                conn_id_todelete.append(pool_id)
        else:
            conn_info = conn_info_iter

    # Close and remove dead connections.
    if len(conn_id_todelete) > 0:
        for pool_id in conn_id_todelete:
            conn_info_iter = db_pool[pool_id]
            conn_info_iter['conn'].close()

            del db_pool[pool_id]

    # Create a new connection.
    if conn_info is None:
        db_pool_id += 1
        conn_info = {
            'conn': MySQLdb.connect(host="localhost", user="thrash-bot", passwd="thrash", db="thrash", charset="utf8"),
            'created': int(time.time()),
            'count': 1,
            'closed': False
        }
        db_pool[db_pool_id] = conn_info
    else:
        conn_info['count'] += 1

    return conn_info


def databaseClose(conn_info):
    conn_info['count'] -= 1

    # Expire old database connections.
    if (conn_info['created'] + 60) < int(time.time()):
        conn_info['closed'] = True

def logMsg(string):
    print("[{}] {}".format(datetime.datetime.now(), string))

    return string

async def send_message(client, channel, text, image_name = None):
    try:
        return await channel.send(context=text)
    except discord.errors.Forbidden:
        logMsg('Could not message user: {}\n{}'.format(channel, text))
        raise
    except:
        logMsg('Failed to send message to channel: {}\n{}'.format(channel, text))

def formatMessage(user_target, message):
    return "*{}*: {}".format(user_target.display_name, message).replace("@", "\{at\}")

""" read a file named fname and return its contents as a string """
def getValueFromFileContents(fname):
	token = ""

	try:
		f_token = open(fname, "r")
		f_token_lines = f_token.readlines()

		for line in f_token_lines:
			line = line.rstrip()
			if len(line) > 0:
				token = line
	except IOError:
		token = ""
		print("Could not read {} file.".format(fname))
	finally:
		f_token.close()

	return token

""" get the Discord API token from the config file on disk """
def getToken():
	return getValueFromFileContents("token")