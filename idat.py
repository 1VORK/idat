import discord

client=discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(m):
    try:
        if m.author.id == 159985870458322944 and m.channel.id == 617560772368924673 and len(m.content) > 15:
            mem = m.mentions[0]
            lvl = int(m.content.split()[18])
    except Exception as e:
        print(e)
