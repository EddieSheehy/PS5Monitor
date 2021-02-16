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

#Webhook Structure for Smyths IE - PS5
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

#Webhook Structure for Smyths IE - Pokemon Shining
def webhookresponsepokemonIE():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths IE", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='Pokemon Shining In Stock', url='https://www.smythstoys.com/ie/en-ie/toys/action-figures-and-playsets/pokemon/pokemon-trading-cards-game/pok%c3%a9mon-trading-card-game-shining-fates-elite-trainer-box/p/196815', color=7419530)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths IE', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url='https://image.smythstoys.com/original/desktop/196815.jpg')
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for Smyths IE - PS5
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

#Webhook Structure for Smyths UK - Pokemon Shining
def webhookresponsepokemonUK():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='Pokemon Shining In Stock', url='https://www.smythstoys.com/uk/en-gb/toys/action-figures-and-playsets/pokemon/pokemon-trading-cards-game/pok%c3%a9mon-trading-card-game-shining-fates-elite-trainer-box/p/196815', color=7419530)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths UK', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url='https://image.smythstoys.com/original/desktop/196815.jpg')
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for Smyths UK
def webhookresponsesmythsDigitalUK():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430', color=15105570)
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
             embed = DiscordEmbed(title='PS5 Disk In Stock', url='https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths UK', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURLDisk)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()
##########################################################################

#PS5DiskGS
def PokemonIELoop():
    while 1:
        winnerSmythsDisk = 0 

        #Smyths
        url = 'https://www.smythstoys.com/ie/en-ie/toys/action-figures-and-playsets/pokemon/pokemon-trading-cards-game/pok%c3%a9mon-trading-card-game-shining-fates-elite-trainer-box/p/196815'
        content = requests.get(url,headers=headers)
        if not content is None:
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockSmythsDisk = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            except:
                webhook = DiscordWebhook(url=webhookurl, username="Smyths IE", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
                embed = DiscordEmbed(title='Shining Trading Cards', url='https://www.smythstoys.com/ie/en-ie/toys/action-figures-and-playsets/pokemon/pokemon-trading-cards-game/pok%c3%a9mon-trading-card-game-shining-fates-elite-trainer-box/p/196815',description='Error Recieved, possible stock', color=15105570)
                webhook.add_embed(embed)
                response = webhook.execute()

        if stockSmythsDisk[53:66] == 'js-enable-btn':
            winnerSmythsDisk = 1
            webhookresponsepokemonIE()
            time.sleep(120)
            winnerSmythsDisk = 0

        else:
            print('1. SmythsIE Pokemon Out of Stock\n')
        
        if winnerSmythsDisk == 1:
            break
        time.sleep(delay)

def PS5DiskSmythsLoop():
    while 1:
        winnerSmythsDisk = 0 

        #Smyths
        url = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'
        content = requests.get(url,headers=headers)
        if not content is None:
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockSmythsDisk = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            except:
                webhook = DiscordWebhook(url=webhookurl, username="Smyths IE", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
                embed = DiscordEmbed(title='PS5 Disk In Stock', url='https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259',description='Error Recieved, possible stock', color=15105570)
                webhook.add_embed(embed)
                response = webhook.execute()

        if stockSmythsDisk[53:66] == 'js-enable-btn':
            winnerSmythsDisk = 1
            webhookresponsesmythsDisk()
            time.sleep(120)
            winnerSmythsDisk = 0

        else:
            print('2. SmythsIE Disk Out of Stock\n')
        
        if winnerSmythsDisk == 1:
            break
        time.sleep(delay)

def PokemonUKLoop():
    while 1:
        winnerSmythsDisk = 0 

        #Smyths
        url = 'https://www.smythstoys.com/uk/en-gb/toys/action-figures-and-playsets/pokemon/pokemon-trading-cards-game/pok%c3%a9mon-trading-card-game-shining-fates-elite-trainer-box/p/196815'
        content = requests.get(url,headers=headers)
        if not content is None:
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockSmythsDisk = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            except:
                webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
                embed = DiscordEmbed(title='Shining Trading Cards In Stock', url='https://www.smythstoys.com/uk/en-gb/toys/action-figures-and-playsets/pokemon/pokemon-trading-cards-game/pok%c3%a9mon-trading-card-game-shining-fates-elite-trainer-box/p/196815',description='Error Recieved, possible stock', color=15105570)
                webhook.add_embed(embed)
                response = webhook.execute()

        if stockSmythsDisk[53:66] == 'js-enable-btn':
            winnerSmythsDisk = 1
            webhookresponsepokemonUK()
            time.sleep(120)
            winnerSmythsDisk = 0

        else:
            print('3. SmythsUK Pokemon Out of Stock\n')
        
        if winnerSmythsDisk == 1:
            break
        time.sleep(delay)

def PS5DigSmythsLoop():
    while 1:
        winnerSmythsDig = 0   

        #Smyths
        url = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430'
        content = requests.get(url, headers=headers)
        if not content is None:
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockSmythsDig = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            except:
                webhook = DiscordWebhook(url=webhookurl, username="Smyths IE", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
                embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430',description='Error Recieved, possible stock', color=15105570)
                webhook.add_embed(embed)
                response = webhook.execute()

        if stockSmythsDig[53:66] == 'js-enable-btn':
            winnerSmythsDig = 1
            webhookresponsesmythsDigitalUK()
            time.sleep(120)
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
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockSmythsDig = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            except:
                webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
                embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430', description='Error Recieved, possible stock', color=15105570)
                webhook.add_embed(embed)
                response = webhook.execute()

        if stockSmythsDig[53:66] == 'js-enable-btn':
            winnerSmythsDig = 1
            webhookresponsesmythsDigitalUK()
            time.sleep(120)
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
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockSmythsDisk = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
            except:
                webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
                embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430',description='Error Recieved, possible stock', color=15105570)
                webhook.add_embed(embed)
                response = webhook.execute()
            
        if stockSmythsDisk[53:66] == 'js-enable-btn':
            winnerSmythsDisk = 1
            webhookresponsesmythsDiskUK()
            time.sleep(120)
            winnerSmythsDisk = 0

        else:
            print('6. SmythsUK Disk Out of Stock\n')
        
        if winnerSmythsDisk == 1:
            break
        time.sleep(delay)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Capitalism Is King'))
    thread1 = Thread(target=PokemonIELoop)
    thread2 = Thread(target=PS5DiskSmythsLoop)
    thread3 = Thread(target=PokemonUKLoop)
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
