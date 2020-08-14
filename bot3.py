from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands
bot = commands.Bot(command_prefix= ".")




@bot.event
async def on_ready():
    print('Bot ready')



@bot.command()
async def laugh(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('laugh.mp3')
    player = voice.play(source)


@bot.command()
async def idc(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('idc.mp3')
    player = voice.play(source)    



bot.run("clientkey-here")    