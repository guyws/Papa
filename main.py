import discord
from discord.ext import commands
from cursing import Curses

from gtts import gTTS

bot = commands.Bot(command_prefix='$')
cr = Curses()
my_id = "740198832905781330"


@bot.event
async def on_ready():
    print("alive")


@bot.event
async def on_message(message):
    if message.content == "cum in":
        await join(message)
        await cr.do_stuff()
    elif message.content == "tf out":
        await leave(message)

    await bot.process_commands(message)


@bot.command()
async def join(ctx):
    print("[DEBUG1]")
    if ctx.author.voice is not None:
        channel = ctx.author.voice.channel
        print("[DEBUG2]")
        vc = await channel.connect()
        print("[DEBUG3]")
        await ctx.channel.send("yelllllllowwwwwwwwwww fuckers")
        vc.play(discord.FFmpegPCMAudio(source="yay.mp3", executable=
        "super seceret path\\ffmpeg-20200831-4a11a6f-win64-static\\ffmpeg-20200831-4a11a6f-win64-static\\bin\\ffmpeg.exe"))
        print("[DEBUG4]")
        await ctx.add_reaction("🍆")
        cr.set_vc(vc)
        print("[DEBUG5]")
    else:
        await ctx.channel.send("tryna trick me, ha? litlle fucker. get in the voice channel before i kill you and your all "
                         "nigerian family")


@bot.command()
async def leave(ctx):
    await ctx.guild.voice_client.disconnect()
    await ctx.channel.send("little cunt")
    await ctx.add_reaction("🖕🏿")

async def check_for_papa(voice_channel):
    members = voice_channel.voice_members
    for member in members:
        if str(member.id) == my_id:
            await cr.say_something("hi papa")

bot.run("BOT TOKEN GOES HERE")
