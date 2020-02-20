import discord
import time
import random

client = discord.Client()
server = discord.Guild
token = ""

import consorts

@client.event
async def on_ready():
    game = discord.Activity(name="END OF THE MONTH", type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.online, activity=game)
    print("server entered")
    print(client.user)

@client.event
async def on_message(message):
    hour = time.gmtime()[3]
    if message.author != client.user:
        if message.content.lower().startswith('!themes'):
            await message.channel.send('https://www.youtube.com/playlist?list=PL_Lh9cF2MSf1AeTsszptxrupK0Zds6S5G')
        elif message.content.lower().startswith('!gamer'):
            await message.channel.send('https://youtu.be/jdtstiuYxis')
        elif message.content.lower().startswith('!munch'):
            await message.channel.send(random.choice(consorts.munchy))
        elif message.content.lower().startswith('!doop'):
            await message.channel.send(random.choice(consorts.doop))
        elif message.content.lower().startswith('!kan'):
            await message.channel.send(random.choice(consorts.kanman))
        elif message.content.lower().startswith('!crocs'):
            await message.channel.send(random.choice(consorts.crocs))
        elif message.content.lower().startswith('!para'):
            await message.channel.send(random.choice(consorts.crocs))
        elif message.content.lower().startswith('!sixten'):
            await message.channel.send(random.choice(consorts.sixten))
        elif message.content.lower().startswith('!juan'):
            await message.channel.send(random.choice(consorts.juan))
        elif message.content.lower().startswith('!nnoby'):
            await message.channel.send(random.choice(consorts.nnoby))
        elif message.content.lower().startswith('!seani'):
            await message.channel.send(random.choice(consorts.scythe))
        elif message.content.lower().startswith('!lateralyst'):
            await message.channel.send(random.choice(consorts.lateralyst))
        elif message.content.lower().startswith('!niboe'):
            await message.channel.send(random.choice(consorts.niboe))
        elif message.content.lower().startswith('!connor'):
            await message.channel.send(random.choice(consorts.connor))
        elif message.content.lower().startswith('!frog'):
            await message.channel.send("who?")
        elif message.content.lower().startswith('!robo'):
            await message.channel.send(random.choice(consorts.robo))
        elif message.content.lower().startswith('!fat'):
            await message.channel.send(random.choice(consorts.fat))
        elif message.content.lower().startswith('!yoshi'):
            await message.channel.send(random.choice(consorts.fat))
        elif message.content.lower().startswith('!king') or message.content.lower().startswith('!krip'):
            await message.channel.send(random.choice(consorts.krip))
        elif message.content.lower().startswith('!m@'):
            await message.channel.send(random.choice(consorts.m))
        elif message.content.lower().startswith('!koff'):
            await message.channel.send(random.choice(consorts.koff))
        elif message.content.lower().startswith('!kab'):
            await message.channel.send(random.choice(consorts.kab))
        elif message.content.lower().startswith('!mal') or message.content.lower().startswith('!swee'):
            await message.channel.send(random.choice(consorts.mal))
        elif message.content.lower().startswith('!mill') or message.content.lower().startswith('!manson'):
            await message.channel.send(random.choice(consorts.miller))
        elif message.content.lower().startswith('!smearg'):
            await message.channel.send("https://img.booru.org/rfck//images/4/41ba24b87681340bf019ce0a1d428ff09701c425.png TEMPORARY")
        elif message.content.lower().startswith('!ethan') or message.content.lower().startswith('!straub'):
            await message.channel.send(random.choice(consorts.ethan))
        elif message.content.lower().startswith('!meat'):
            await message.channel.send(random.choice(consorts.meaty))
        elif message.content.lower().startswith('!kiwanuka'):
            await message.channel.send("https://www.michaelkiwanuka.com/")
        elif message.content.startswith('!vr'):
            await message.channel.send("https://img.booru.org/rfck//images/4/067d0e3463903d422f6864d2b2596ad723153406.gif")
        elif message.content.startswith('!VR'):
            await message.channel.send("https://cdn.discordapp.com/attachments/431237299137675297/643549838469758976/MUNCHY_SPEEEEEEEEEEEEEEEEEEEEEEEEEEEEN.mp4")
        elif message.content.startswith('**!VR'):
            await message.channel.send("https://cdn.discordapp.com/attachments/504897783287906304/643959817588965376/MUNCHY_SPEEEEEEEEEEEEN_BOOST.mp4")
        elif message.content.lower().startswith('!goodboy'):
            await message.channel.send("https://img.booru.org/rfck//images/1/93c3572a5ae571efe866620cc0c744147d597c24.jpg")
        elif message.content.lower().startswith('!whosright'):
            await message.channel.send("milIer is right!!!!")
        elif message.content.lower().startswith('!laugh'):
            emp1 = discord.utils.get(message.guild.emojis, name="etlaugh")
            await message.channel.send(emp1)
        elif message.content.lower().startswith('!modelo'):
            await message.channel.send('https://youtube.com/watch?v=Gd9P378edq4')
        elif message.content.lower().startswith('!vibecheck'):
            if random.randint(1, 2) == 1:
                response = "yeaaah.. they aint vibin..."
            else:
                response = "oh they vibin hard!!!!"
            await message.channel.send(response)
        elif message.content.lower().startswith('!data') or message.content.lower().startswith('!slime'):
            if len(message.mentions) == 1:
                await message.channel.send('https://ew.krakissi.net/stats/player.html?pl={}'.format(str(message.mentions[0].id)))
            else:
                await message.channel.send('https://ew.krakissi.net/stats/player.html?pl={}'.format(str(message.author.id)))
        elif message.content.lower().startswith('!thrash'):
            emp1 = discord.utils.get(message.guild.emojis, name="blank")
            emp2 = discord.utils.get(message.guild.emojis, name="rf")
            emp3 = discord.utils.get(message.guild.emojis, name="s1")
            emp4 = discord.utils.get(message.guild.emojis, name="munchy")
            emp5 = discord.utils.get(message.guild.emojis, name="s3")
            em1 = str(emp1)
            em2 = str(emp2)
            em3 = str(emp3)
            em4 = str(emp4)
            em5 = str(emp5)
            n = '\n'
            thrash = em1 + em1 + em1 + em2 + em5 + em3 + em5 + em2 + em2 + em3 + em3 + em5 + em3 + em2 + n + em1 + em1 + em2 + em2 + em3 + em2 + em2 + em3 + em2 + em5 + em2 + em2 + em2 + em2 + em2 + n + em4 + em2 + em2 + em2 + em5 + em3 + em5 + em3 + em2 + em5 + em3 + em3 + em2 + em2 + em2 + em2 + em4 + n + em1 + em1 + em2 + em2 + em3 + em2 + em5 + em2 + em2 + em5 + em2 + em2 + em2 + em2 + em2 + n + em1 + em1 + em1 + em2 + em3 + em2 + em2 + em3 + em2 + em3 + em2 + em2 + em2 + em2
            await message.channel.send('*' + message.author.display_name + '*:\n' + thrash)
        elif message.content.lower().startswith('!doublethrash'):
            emp1 = discord.utils.get(message.guild.emojis, name="blank")
            emp2 = discord.utils.get(message.guild.emojis, name="rf")
            emp3 = discord.utils.get(message.guild.emojis, name="s1")
            emp4 = discord.utils.get(message.guild.emojis, name="munchy")
            emp5 = discord.utils.get(message.guild.emojis, name="s3")
            em1 = str(emp1)
            em2 = str(emp2)
            em3 = str(emp3)
            em4 = str(emp4)
            em5 = str(emp5)
            n = '\n'
            thrash = em1 + em1 + em1 + em2 + em5 + em3 + em5 + em2 + em2 + em3 + em3 + em5 + em3 + em2 + n + em1 + em1 + em2 + em2 + em3 + em2 + em2 + em3 + em2 + em5 + em2 + em2 + em2 + em2 + em2 + n + em4 + em2 + em2 + em2 + em5 + em3 + em5 + em3 + em2 + em5 + em3 + em3 + em2 + em2 + em2 + em2 + em4 + n + em1 + em1 + em2 + em2 + em3 + em2 + em5 + em2 + em2 + em5 + em2 + em2 + em2 + em2 + em2 + n + em1 + em1 + em1 + em2 + em3 + em2 + em2 + em3 + em2 + em3 + em2 + em2 + em2 + em2
            await message.channel.send('*' + message.author.display_name + '*:\n' + thrash, delete_after=90)
            await message.channel.send('*' + message.author.display_name + '*:\n' + thrash, delete_after=90)
        elif message.content.lower().startswith('!quadthrash'):
            emp1 = discord.utils.get(message.guild.emojis, name="blank")
            emp2 = discord.utils.get(message.guild.emojis, name="rf")
            emp3 = discord.utils.get(message.guild.emojis, name="s1")
            emp4 = discord.utils.get(message.guild.emojis, name="munchy")
            emp5 = discord.utils.get(message.guild.emojis, name="s3")
            em1 = str(emp1)
            em2 = str(emp2)
            em3 = str(emp3)
            em4 = str(emp4)
            em5 = str(emp5)
            n = '\n'
            thrash = em1 + em1 + em1 + em2 + em5 + em3 + em5 + em2 + em2 + em3 + em3 + em5 + em3 + em2 + n + em1 + em1 + em2 + em2 + em3 + em2 + em2 + em3 + em2 + em5 + em2 + em2 + em2 + em2 + em2 + n + em4 + em2 + em2 + em2 + em5 + em3 + em5 + em3 + em2 + em5 + em3 + em3 + em2 + em2 + em2 + em2 + em4 + n + em1 + em1 + em2 + em2 + em3 + em2 + em5 + em2 + em2 + em5 + em2 + em2 + em2 + em2 + em2 + n + em1 + em1 + em1 + em2 + em3 + em2 + em2 + em3 + em2 + em3 + em2 + em2 + em2 + em2
            await message.channel.send('*' + message.author.display_name + '*:\n' + thrash, delete_after=90)
            await message.channel.send('*' + message.author.display_name + '*:\n' + thrash, delete_after=90)
            await message.channel.send('*' + message.author.display_name + '*:\n' + thrash, delete_after=90)
            await message.channel.send('*' + message.author.display_name + '*:\n' + thrash, delete_after=90)
        elif message.content.lower().startswith('!album'):
            await message.channel.send('https://www.youtube.com/watch?v=6Bx5vWEoGpA\n\nIf you want to listen to the full thing uncopyright struck: https://thetobedecided.bandcamp.com/album/rowdy-power-album')
        elif message.content.lower().startswith('!takedown'):
            await message.channel.send("https://cdn.discordapp.com/attachments/522236656086941736/638174609719427090/mathew-thumbs-down.gif")
        elif message.content.lower().startswith('!freak'):
            if random.randrange(0,2) == 1:
                await message.channel.send("https://cdn.discordapp.com/attachments/633521717444345857/633522227123322901/freddy_freaker2.gif")
            else:
                await message.channel.send("1-900-490 FREAK")
        elif message.content.lower().startswith('!:maidsorts:'):
            await message.channel.send(random.choice(consorts.kanman))

client.run(token)
