#!/usr/bin/python3

import discord
import time
import random
import shlex
import sys
import asyncio
import os

import utils
import cfg
import cmd

from thrasher import Thrasher

utils.logMsg('Starting up...')
init_complete = False

client = discord.Client()

# Map of all command words in the game to their implementing function.
cmd_map = {
    cfg.cmd_thrash: cmd.thrash,
    cfg.cmd_doublethrash: cmd.double_thrash,
    cfg.cmd_triplethrash: cmd.triple_thrash,
    cfg.cmd_quadruplethrash: cmd.quadruple_thrash,
    cfg.cmd_quadruplethrash_alt1: cmd.quadruple_thrash,
    cfg.cmd_quintuplethrash: cmd.quintuple_thrash,
    cfg.cmd_quintuplethrash_alt1: cmd.quintuple_thrash,
    cfg.cmd_sextuplethrash: cmd.sextuple_thrash,
    cfg.cmd_sextuplethrash_alt1: cmd.sextuple_thrash,
    cfg.cmd_septuplethrash: cmd.septuple_thrash,
    cfg.cmd_septuplethrash_alt1: cmd.septuple_thrash,
    cfg.cmd_takedown: cmd.takedown,
    cfg.cmd_themes: cmd.themes,
    cfg.cmd_gamering: cmd.gamering,
    cfg.cmd_frog: cmd.frog,
    cfg.cmd_goodboy: cmd.goodboy,
    cfg.cmd_laughtrack: cmd.laughtrack,
    cfg.cmd_modelo: cmd.modelo,
    cfg.cmd_vibecheck: cmd.vibecheck,
    cfg.cmd_thrashcoin: cmd.thrashcoin,
    cfg.cmd_thrashcoin_alt1: cmd.thrashcoin,
    cfg.cmd_thrashcoin_alt2: cmd.thrashcoin,
    cfg.cmd_leaderboard: cmd.leaderboard,
    cfg.cmd_kanman: cmd.kanman,
    cfg.cmd_miller: cmd.miller,
}

@client.event
async def on_ready():
    global init_complete
    if init_complete:
        return
    init_complete = True
    cfg.set_client(client)
    utils.logMsg('Logged in as {} ({}).'.format(client.user.name, client.user.id))

    try:
        await client.change_presence(activity="!THRASH")
    except:
        utils.logMsg("Failed to change_presence!")

    utils.logMsg('Ready.')

    """
        Set up for infinite loop to perform periodic tasks.
    """
    time_now = int(time.time())

    # Every three hours we log a message saying the periodic task hook is still active. On startup, we want this to happen within about 60 seconds, and then on the normal 3 hour interval.
    time_last_logged = time_now - cfg.update_hookstillactive + 60

    stream_live = None

    utils.logMsg('Beginning periodic hook loop.')
    while not utils.TERMINATE:
        time_now = int(time.time())

        # Periodic message to log that this stuff is still running.
        if (time_now - time_last_logged) >= cfg.update_hookstillactive:
            time_last_logged = time_now

            utils.logMsg("Periodic hook still active.")

        # Update thrash coin counts in database
        if len(cmd.thrashcoin_queue) != 0:
            for thrasher in cmd.thrashcoin_queue.keys():
                user_data = Thrasher(id_user = thrasher)
                user_data.thrashcoin += cmd.thrashcoin_queue[thrasher]
                user_data.persist()
                cmd.thrashcoin_queue[thrasher] = 0

            utils.logMsg('Thrashcoin updated.')

        # Wait a while before running periodic tasks.
        await asyncio.sleep(900)



@client.event
async def on_message(message):
    cfg.set_client(client)

    """ do not interact with our own messages """
    if message.author.id == client.user.id or message.author.bot == True:
        return

    if message.content.startswith(cfg.cmd_prefix):
        """
            Wake up if we need to respond to messages. Could be:
                message starts with !
                direct message (server == None)
                user is new/has no roles (len(roles) < 2)
                user is swearing
        """

        # tokenize the message. the command should be the first word.
        try:
            tokens = shlex.split(
                message.content)  # it's split with shlex now because shlex regards text within quotes as a single token
        except:
            tokens = message.content.split(
                ' ')  # if splitting via shlex doesnt work (odd number of quotes), use the old splitting method so it doesnt give an exception

        tokens_count = len(tokens)
        command = tokens[0].lower() if tokens_count >= 1 else ""

        # remove mentions to us
        mentions = list(filter(lambda user: user.id != client.user.id, message.mentions))

        # Create command object
        cmd_obj = cmd.ThrashCmd(
            tokens=tokens,
            message=message,
            client=client,
            mentions=mentions
        )

        # if the message wasn't a command, we can stop here
        if not message.content.startswith(cfg.cmd_prefix):
            return

        # Check if its a booru list command.
        booru = False

        if message.content not in ("!miller", "!kanman"):
            for name in cfg.booru_commands.keys():
                if message.content.startswith(name):
                    booru = True
                    booru_list = cfg.booru_commands[name]

        # Check the main command map for the requested command.
        global cmd_map
        cmd_fn = cmd_map.get(command)

        if cmd_fn is not None:
            # Execute found command
            return await cmd_fn(cmd_obj)

        elif booru:
            return await cmd.link_image(cmd_obj, booru_list)

# find our REST API token
token = utils.getToken()

if token == None or len(token) == 0:
    utils.logMsg('Please place your API token in a file called "token", in the same directory as this script.')
    sys.exit(0)

# connect to discord and run indefinitely
try:
    client.run(token)
finally:
    utils.TERMINATE = True
    utils.logMsg("main thread terminated.")
