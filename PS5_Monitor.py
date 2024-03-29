import requests
import bs4 as bs
import time
import discord
from discord_webhook import *
from threading import Thread
from proxycrawl import CrawlingAPI, ScraperAPI, LeadsAPI

TOKEN = "NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.RsuGF9pIAtU3dguVz7-EclQRy34"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
client = discord.Client()
webhookurl = 'https://discord.com/api/webhooks/725833804899418143/ahah5olFVarkj3b0hPQK8MTf95qKc5p6EWXdQDelhYJ-oJuZFK584MITLM15TYbkxH-T'
imgURLDisk = 'https://static-ie.gamestop.ie/images/products/271916/3max.jpg'
imgURLDig = 'https://static-ie.gamestop.ie/images/products/275145/3max.jpg'
api = CrawlingAPI({ 'token': '7VZvcH3_-_3fvR7fnXF5sw' })
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

def CapsulatedTest():
    print('Capsulated Started')
    while 1:
        url = URL
        result = requests.get(url, headers=headers)
        soup = bs.BeautifulSoup(result.text, 'lxml')
        try:
            info = soup.find("iframe")
            infocheck = info.text
            if "Incapsula" in infocheck:
                print('Incapsula Error')
                s = requests.Session()
                print('bye')
                print('[STATUS] - Adding Cookies')
                CapsulatedTest()
                print('Passed For Loop')
                result = requests.get(url, headers=headers, cookies=cookie)
                soup = bs.BeautifulSoup(result.text, 'lxml')   
            else:
                PS5DiskSmythsLoop()
        except:
            PS5DiskSmythsLoop()

#PS5DiskGS
def PS5DiskGSLoop():

    while 1:
        winnerGSDisk = 0
        title = 'PS5 Disk In Stock'
        #GameStop
        url = 'https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console'
        content = requests.get(url,headers=headers)
        if not content is None:
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockGSDisk = soup.find("div", {"class": "bigBuyButtons SPNOpenMap"}).find('a').text

                if stockGSDisk == 'Out Of Stock':
                    print('1. GamestopIE Disk Out Of Stock P1\n')

                else:
                    winnerGSDisk = 1
                    webhookresponsegamestopDisk()
                    time.sleep(120)
                    winnerGSDisk = 0

                if winnerGSDisk == 1:
                    break
                time.sleep(delay)
            except:
                print('1. Gamestop IE Disk Out Of Stock P2\n')
                time.sleep(delay)
                    



def PS5DiskSmythsLoop():
    while 1:
        winnerSmythsDisk = 0 

        
        #Smyths
        url = "https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259"
        result = requests.get(url, headers=headers)

        try:
            info = soup.find("iframe")
            infocheck = info.text
            print(infocheck)
            if "Incapsula" in infocheck:
                CapsulatedTest()
        except:
            continue

        if not result is None:
            try:
                soup = bs.BeautifulSoup(result, 'lxml')
                stockSmythsDisk = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))

                if stockSmythsDisk[53:66] == 'js-enable-btn':
                    winnerSmythsDisk = 1
                    webhookresponsesmythsDisk()
                    time.sleep(120)
                    winnerSmythsDisk = 0

                else:
                    print('2. SmythsIE Disk Out of Stock P1\n')
                
                if winnerSmythsDisk == 1:
                    break
                time.sleep(delay)
            except:
                print('2. SmythsIE Disk Out Of Stock P2\n')
                time.sleep(delay)



def PS5DigGSLoop():
    while 1:
        winnerGSDig = 0    

        #GameStop
        url = 'https://www.gamestop.ie/PlayStation%205/Games/74863/playstation-5-digital-edition-console'
        content = requests.get(url, headers=headers)
        if not content is None:
            try:
                soup = bs.BeautifulSoup(content.text, 'lxml')
                stockGSDig = soup.find("div", {"class": "bigBuyButtons SPNOpenMap"}).find('a').text

                if stockGSDig == 'Out Of Stock':
                    print('3. GamestopIE Digital Out Of Stock P1\n')

                else:
                    winnerGSDig = 1
                    webhookresponsegamestopDigital()
                    time.sleep(120)
                    winnerGSDig = 0

                if winnerGSDig == 1:
                    break
                time.sleep(delay)
            except:
                print('3. GamestopIE Digital Out Of Stock P2\n')
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

                if stockSmythsDig[53:66] == 'js-enable-btn':
                    winnerSmythsDig = 1
                    webhookresponsesmythsDigitalUK()
                    time.sleep(120)
                    winnerSmythsDig = 0

                else:
                    print('4. SmythsIE Digital Out of Stock P1\n')
                
                if winnerSmythsDig == 1:
                    break
                time.sleep(delay)
            except:
                print('4. SmythsIE Digital Out of Stock P2\n')
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

                if stockSmythsDig[53:66] == 'js-enable-btn':
                    winnerSmythsDig = 1
                    webhookresponsesmythsDigitalUK()
                    time.sleep(120)
                    winnerSmythsDig = 0

                else:
                    print('5. SmythsUK Digital Out of Stock P1\n')
                
                if winnerSmythsDig == 1:
                    break
                time.sleep(delay)
            except:
                print('5. SmythsUK Digital Out of StockP2\n')
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
                        
                if stockSmythsDisk[53:66] == 'js-enable-btn':
                    winnerSmythsDisk = 1
                    webhookresponsesmythsDiskUK()
                    time.sleep(120)
                    winnerSmythsDisk = 0

                else:
                    print('6. SmythsUK Disk Out of Stock P1\n')
                
                if winnerSmythsDisk == 1:
                    break
                time.sleep(delay)
            except:
                print('6. SmythsUK Disk Out of Stock P2\n')
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
