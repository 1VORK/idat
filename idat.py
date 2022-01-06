import discord
from discord.utils import get

client=discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(m):
    if m.author.id == 159985870458322944 and m.channel.id == 617560772368924673 and len(m.content) > 15:
        mem = m.mentions[0]
        lvl = int(m.content.split()[18])
        if lvl > 99:
            await mem.add_role(get(m.guild.roles, id=0))
        elif lvl > 89:
            await mem.add_role(get(m.guild.roles, id=0))
        elif lvl > 79:
            await mem.add_role(get(m.guild.roles, id=0))
        elif lvl > 69:
            await mem.add_role(get(m.guild.roles, id=0))
        elif  lvl > 59:
            await mem.add_role(get(m.guild.roles, id=0))
        elif lvl > 49:
            await mem.add_role(get(m.guild.roles, id=0))
        elif lvl > 39:
            await mem.add_role(get(m.guild.roles, id=0))
        elif lvl > 29:
            await mem.add_role(get(m.guild.roles, id=0))
        elif lvl > 19:
            await mem.add_role(get(m.guild.roles, id=531217764145430528))
        elif lvl > 9:
            await mem.add_role(get(m.guild.roles, id=617654956845170701))
        elif lvl > 4:
            await mem.add_role(get(m.guild.roles, id=531214594480406548))

client.run(open('tokens/idat','r').read())
