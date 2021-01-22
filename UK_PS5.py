import requests
import bs4 as bs
import time
import discord
from discord_webhook import *

TOKEN = "NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.RsuGF9pIAtU3dguVz7-EclQRy34"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
client = discord.Client()
webhookurl = 'https://discord.com/api/webhooks/800840213135228948/DpuqgulYFHYHuQhgy7g-NVj78E6H9kE6dgvQHdzHmX5EWzWVh45ck0AJT5RIupjYgeIr'
imgURL = 'https://static-ie.gamestop.ie/images/products/275145/3max.jpg'

#Webhook Structure for Smyths UK
def webhookresponsesmythsdigital():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths UK', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURL)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

def webhookresponsesmythsdisk():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths UK", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Disk In Stock', url='https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths UK', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURL)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

@client.event
async def on_ready():

    winnerDisk = 0
    winnerDigital = 0

    while 1:

        #Smyths
        urlSmyths = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430'
        content = requests.get(urlSmyths,headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockSmyths = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
          
        if stockSmyths[53:66] == 'js-enable-btn':
            winnerDigital = 1
            webhookresponsesmythsdigital()
            time.sleep(30)
            winnerDigital = 0

        else:
            print('Smyths UK Digital Out of Stock\n')
        
        #Smyths
        urlSmyths = 'https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'
        content = requests.get(urlSmyths,headers=headers)
        if not content is None:
            soup = bs.BeautifulSoup(content.text, 'lxml')
            stockSmyths = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
          
        if stockSmyths[53:66] == 'js-enable-btn':
            winnerDisk = 1
            webhookresponsesmyths()
            time.sleep(30)
            winnerDisk = 0

        else:
            print('Smyths UK Disk Out of Stock\n')
     
        if winnerDisk and winnerDigital == 1:
            break
        time.sleep(3)

client.run(TOKEN)