from datetime import date, datetime
import discord
import time
from discord.ext import commands
client = discord.Client()
client = commands.Bot("! ")
@client.event
async def on_ready():
    print(f"Ben hazırım - {client.user.name}.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.unknown,
                                                           name="python_help. Bu bot 9. koğuştaki mucize ekibi tarafından yapıldı."))
@client.command(name="alarm")
async def echo(ctx, *, message=None):
    message = message or "Lütfen devamında dakika girin!"
    try:
        x = int(message)
    except:
        await ctx.send("Sayı girin!")
        return

    await ctx.message.delete()
    await ctx.send(message + f" dakika sonra öteceğim {ctx.author.mention}.")
    nowa = datetime.now()
    deger = int(nowa.minute) + int(message)
    while deger > 60:
        nowa.hour += 1
        deger -= 60

    await  ctx.send("Alarm zamanı: %s:%s" % (nowa.hour, deger))
    while not (nowa.hour == datetime.now().hour and deger == datetime.now().minute and datetime.now().second == nowa.second):
        a = 1
    await ctx.send(f"Süre doldu {ctx.author.mention} bi bi bi bip!")

client.run("bot tokeni")
