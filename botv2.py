# Ekip-9 projesi
from datetime import date, datetime
import asyncio
import discord
import time
import sys
from discord.ext import commands
# Bol keseden kütüphane aldım 1-2 tanesini kullanmamış olabilirim.
client = discord.Client()
client = commands.Bot("!")


class Error(Exception):
    pass
    # Hata ismi oluşturdum. NegativeError diye bir şey aslında yok.

class NegativeError(Error):
    pass

@client.event
async def on_ready():
    print(f"Ben hazırım - {client.user.name}.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
    name="Bu bot 9. koğuştaki mucize ekibi tarafından yapıldı."))  # Buranın nasıl çalıştığını tam anlamadım ama güzel diye koydum. Botun açıklamasına ekliyor bunu.
   
@client.command(name="kur", aliases=["alarm", "alarmkur", "set"])  # 4 çeşit komut belirledim.
async def echo(ctx, *, minutes=None): # Normalde echo aynı şeyi döndürmek için kullanılıyor ama ben böyle yapıp geçtim.

    try:

        an = datetime.now()  # Komutu verdiğimiz anı kaydediyor.
        minuteint = int(minutes)
        if minuteint <= 0:  # 0'ın altında bir değer girdiysek hata mesajı veriyor.
            messagenegative = "| Negatif sayımı?¿"
            messagenegative2 = await ctx.send(messagenegative)
            myError = NegativeError
            raise myError
        await ctx.message.delete() # Bizim girdiğimiz değeri siliyor. Kanalın temiz olması için böyle yaptım.
        ilkmesaj = await ctx.send(f"| Süre {minutes} dk olarak ayarlandı.")
        an2 = minuteint + an.minute
        an3 = minuteint + an.minute
        an4 = an.second
        while minuteint + an.minute > 60:
            an.hour += 1
            an2 -= 60
        z = 0
        messagemention = await ctx.send(f"| {ctx.author.mention}") # Büyük sunucularda kullanılabilmesi için bunu ekledim. Karışıklık olmasın diye.
        messagebiter = await ctx.send(f"| {minutes} dk kaldı.") # Kaç dakika kaldığını takip edebiliyoruz. Dikkat dağıtıcı olmaması açısından saniye koymadım.
        while True:
            if an4 == datetime.now().second:
                if an.hour == datetime.now().hour and an2 == datetime.now().minute:
                    await messagebiter.edit(content="| Süre doldu!")
                    z = 1
            if z == 1:
                break
            arda = datetime.now().hour
            x = 0

            while an.hour > arda:
                x += 60
                arda += 1

            if an.hour == arda:
                x = 0

            await messagebiter.edit(content=f"| {an3 + x - datetime.now().minute} dk kaldı.") # Her dakikada 1 yazıyı editliyor.

        message9 = ctx.author.mention
        message7 = await ctx.send(f"| {message9}, Sayacın bitti!")
        await asyncio.sleep(5)
        await messagebiter.delete() # Tek tek tüm mesajları silerek sayfanın temiz olmasını sağlıyor.
        await message7.delete() # Tek tek tüm mesajları silerek sayfanın temiz olmasını sağlıyor.
        await messagemention.delete() # Tek tek tüm mesajları silerek sayfanın temiz olmasını sağlıyor.
        await ilkmesaj.delete() # Tek tek tüm mesajları silerek sayfanın temiz olmasını sağlıyor.
    except NegativeError:
        messagepozi = "| Pozitif sayı Giriniz!" # Negatif sayı girilirse buraya atıyor.
        messagepozi2 = await ctx.send(messagepozi)
        await asyncio.sleep(5)
        await messagepozi2.delete()
        await messagenegative2.delete()
        await ctx.message.delete()
    except ValueError:
        messagesayi = "| Sayı Giriniz!" # Sayı girilmezse buraya atıyor.
        messagesayi2 = await ctx.send(messagesayi)
        await asyncio.sleep(5)
        await messagesayi2.delete()
        await ctx.message.delete()

client.run("Token girin")
