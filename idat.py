import discord
from discord.utils import get

client=discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(m):
    if m.author.id == 159985870458322944 and m.channel.id == 617560772368924673 and len(m.content) > 15:
        mem = m.mentions[0]
        lvl = int(m.content.split()[18])
        if lvl > 99:
            await mem.add_roles(get(m.guild.roles, id=0)) #ant
        elif lvl > 89:
            await mem.add_roles(get(m.guild.roles, id=772193415802388500)) #outside
        elif lvl > 79:
            await mem.add_roles(get(m.guild.roles, id=772192532401750017)) #spoon
        elif lvl > 69:
            await mem.add_roles(get(m.guild.roles, id=609437506714206215)) #crocs
        elif  lvl > 59:
            await mem.add_roles(get(m.guild.roles, id=617923744811319317)) #crayf
        elif lvl > 49:
            await mem.add_roles(get(m.guild.roles, id=617923740117762088)) #manc
        elif lvl > 39:
            await mem.add_roles(get(m.guild.roles, id=609459315916406847)) #bee
        elif lvl > 29:
            await mem.add_roles(get(m.guild.roles, id=617923748737187858)) #crab
        elif lvl > 19:
            await mem.add_roles(get(m.guild.roles, id=531217764145430528)) #hyd
        elif lvl > 9:
            await mem.add_roles(get(m.guild.roles, id=617654956845170701)) #mag
        elif lvl > 4:
            await mem.add_roles(get(m.guild.roles, id=531214594480406548)) #frog

client.run(open('tokens/idat','r').read())
