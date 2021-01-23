import requests
import bs4 as bs
import time
import discord
from discord_webhook import *
from threading import Thread

TOKEN = "NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.RsuGF9pIAtU3dguVz7-EclQRy34"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
client = discord.Client()
webhookurl = 'https://discord.com/api/webhooks/800840213135228948/DpuqgulYFHYHuQhgy7g-NVj78E6H9kE6dgvQHdzHmX5EWzWVh45ck0AJT5RIupjYgeIr'
imgURLDisk = 'https://static-ie.gamestop.ie/images/products/271916/3max.jpg'
imgURLDig = 'https://static-ie.gamestop.ie/images/products/275145/3max.jpg'
delay = 6

#Webhook Structure for Smyths IE
def webhookresponsesmythsDisk():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths IE", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Disk In Stock', url='https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths IE', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURLDisk)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for GameStop IE
def webhookresponsegamestopDisk():
             webhook = DiscordWebhook(url=webhookurl, username="Gamestop IE", avatar_url='https://jobapplications.net/wp-content/uploads/gamestop-logo-icon.png')
             embed = DiscordEmbed(title='PS5 Disk In Stock', url='https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console', color=7419530)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Gamestop IE', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURLDisk)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for Smyths IE
def webhookresponsesmythsDigital():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths IE", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths IE', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURLDig)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for GameStop IE
def webhookresponsegamestopDigital():
             webhook = DiscordWebhook(url=webhookurl, username="Gamestop IE", avatar_url='https://jobapplications.net/wp-content/uploads/gamestop-logo-icon.png')
             embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.gamestop.ie/PlayStation%205/Games/74863/playstation-5-digital-edition-console', color=7419530)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Gamestop IE', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURLDig)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for Smyths UK
def webhookresponsesmythsDigitalUK():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths UK', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURLDig)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for Smyths UK
def webhookresponsesmythsDiskUK():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Disk In Stock', url='https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths UK', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURLDisk)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()
##########################################################################

#PS5DiskGS
def PS5DiskGSLoop():

    while 1:
        winnerGSDisk = 0
        title = 'PS5 Disk In Stock'
        #GameStop
        url = 'https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console'
        content = requests.get(url,headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockGSDisk = soup.find("div", {"class": "bigBuyButtons SPNOpenMap"}).find('a').text

        if stockGSDisk == 'Out Of Stock':
            print('1. GamestopIE Disk Out Of Stock\n')

        else:
            winnerGSDisk = 1
            webhookresponsegamestopDisk()
            time.sleep(30)
            winnerGSDisk = 0

        if winnerGSDisk == 1:
            break
        time.sleep(delay)

def PS5DiskSmythsLoop():
    while 1:
        winnerSmythsDisk = 0 

        #Smyths
        url = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'
        content = requests.get(url,headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockSmythsDisk = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            
        if stockSmythsDisk[53:66] == 'js-enable-btn':
            winnerSmythsDisk = 1
            webhookresponsesmythsDisk()
            time.sleep(30)
            winnerSmythsDisk = 0

        else:
            print('2. SmythsIE Disk Out of Stock\n')
        
        if winnerSmythsDisk == 1:
            break
        time.sleep(delay)

def PS5DigGSLoop():
    while 1:
        winnerGSDig = 0    

        #GameStop
        url = 'https://www.gamestop.ie/PlayStation%205/Games/74863/playstation-5-digital-edition-console'
        content = requests.get(url, headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockGSDig = soup.find("div", {"class": "bigBuyButtons SPNOpenMap"}).find('a').text

        if stockGSDig == 'Out Of Stock':
            print('3. GamestopIE Digital Out Of Stock\n')

        else:
            winnerGSDig = 1
            webhookresponsegamestopDigital()
            time.sleep(30)
            winnerGSDig = 0

        if winnerGSDig == 1:
            break
        time.sleep(delay)

def PS5DigSmythsLoop():
    while 1:
        winnerSmythsDig = 0   

        #Smyths
        url = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430'
        content = requests.get(url, headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockSmythsDig = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))

        if stockSmythsDig[53:66] == 'js-enable-btn':
            winnerSmythsDig = 1
            webhookresponsesmythsDigitalUK()
            time.sleep(30)
            winnerSmythsDig = 0

        else:
            print('4. SmythsIE Digital Out of Stock\n')
        
        if winnerSmythsDig == 1:
            break
        time.sleep(delay)

def PS5DigSmythsLoopUK():
    while 1:
        winnerSmythsDig = 0   

        #Smyths
        url = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430'
        content = requests.get(url, headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockSmythsDig = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))

        if stockSmythsDig[53:66] == 'js-enable-btn':
            winnerSmythsDig = 1
            webhookresponsesmythsDigitalUK()
            time.sleep(30)
            winnerSmythsDig = 0

        else:
            print('5. SmythsUK Digital Out of Stock\n')
        
        if winnerSmythsDig == 1:
            break
        time.sleep(delay)

def PS5DiskSmythsLoopUK():
    while 1:
        winnerSmythsDisk = 0 

        #Smyths
        url = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'
        content = requests.get(url,headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockSmythsDisk = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            
        if stockSmythsDisk[53:66] == 'js-enable-btn':
            winnerSmythsDisk = 1
            webhookresponsesmythsDisk()
            time.sleep(30)
            winnerSmythsDisk = 0

        else:
            print('6. SmythsUK Disk Out of Stock\n')
        
        if winnerSmythsDisk == 1:
            break
        time.sleep(delay)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Capitalism Is King'))
    thread1 = Thread(target=PS5DiskGSLoop)
    thread2 = Thread(target=PS5DiskSmythsLoop)
    thread3 = Thread(target=PS5DigGSLoop)
    thread4 = Thread(target=PS5DigSmythsLoop)
    thread5 = Thread(target=PS5DigSmythsLoopUK)
    thread6 = Thread(target=PS5DiskSmythsLoopUK)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
client.run(TOKEN)
