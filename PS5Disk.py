import requests
import bs4 as bs
import time
import discord
from discord_webhook import *

TOKEN = "NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.RsuGF9pIAtU3dguVz7-EclQRy34"

client = discord.Client()
webhookurl = 'https://discord.com/api/webhooks/800840213135228948/DpuqgulYFHYHuQhgy7g-NVj78E6H9kE6dgvQHdzHmX5EWzWVh45ck0AJT5RIupjYgeIr'
imgURL = 'https://static-ie.gamestop.ie/images/products/275145/3max.jpg'

#Webhook Structure for Smyths IE
def webhookresponsesmyths():
             webhook = DiscordWebhook(url=webhookurl, username="Smyths IE", avatar_url='https://pbs.twimg.com/profile_images/1201814930581868544/f0N7G3DI_400x400.png')
             embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-digital-edition-console/p/191430', color=15105570)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Smyths IE', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURL)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

#Webhook Structure for GameStop IE
def webhookresponsegamestop():
             webhook = DiscordWebhook(url=webhookurl, username="Gamestop IE", avatar_url='https://jobapplications.net/wp-content/uploads/gamestop-logo-icon.png')
             embed = DiscordEmbed(title='PS5 Digital In Stock', url='https://www.gamestop.ie/PlayStation%205/Games/74863/playstation-5-digital-edition-console', color=7419530)
             embed.add_embed_field(name='Type', value='Restock', inline=True)
             embed.add_embed_field(name='Site', value='Gamestop IE', inline=True)
             embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png')
             embed.set_thumbnail(url=imgURL)
             embed.set_timestamp()
             webhook.add_embed(embed)
             response = webhook.execute()

@client.event
async def on_ready():

    winner  = 0

    while 1:
        
        #GameStop
        urlGS = 'https://www.gamestop.ie/PlayStation%205/Games/74863/playstation-5-digital-edition-console'
        content = requests.get(urlGS)
        soup = bs.BeautifulSoup(content.text, 'lxml')
        stockGS = soup.find("div", {"class": "bigBuyButtons SPNOpenMap"}).find('a').text

        #Smyths
        urlSmyths = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'
        content = requests.get(urlSmyths)
        soup = bs.BeautifulSoup(content.text, 'lxml')
        stockSmyths = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
        if stockGS == 'Out Of Stock':
            print('Gamestop Disk Out Of Stock\n')

        else:
            winner = 1
            webhookresponsegamestop()
            time.sleep(30)
            winner = 0

        if stockSmyths[53:66] == 'js-enable-btn':
            winner = 1
            webhookresponsesmyths()
            time.sleep(30)
            winner = 0

        else:
            print('Smyths Disk Out of Stock\n')
     
        if winner == 1:
            break
        time.sleep(3)

client.run(TOKEN)
