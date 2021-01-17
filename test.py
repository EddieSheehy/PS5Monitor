import requests
import bs4 as bs
import time
import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix =  '!')
TOKEN = "NzExMjU2NjU4NTkyMTM3MjM3.XsAXYQ.RsuGF9pIAtU3dguVz7-EclQRy34"

@client.event
async def on_ready():
    print("Bot Ready")

    imgURL = 'https://i.guim.co.uk/img/media/f58aa676496e9eaba611000477f28d0232fd91eb/0_165_3378_2027/master/3378.jpg?width=620&quality=45&auto=format&fit=max&dpr=2&s=e8c5338394932059caf20ba2516be828'

    winner  = 0

    while 1:
        
        #GameStop
        urlGS = 'https://www.gamestop.ie/PlayStation%205/Games/72504/playstation-5-console'
        content = requests.get(urlGS)
        soup = bs.BeautifulSoup(content.text, 'lxml')
        stockGS = soup.find("div", {"class": "bigBuyButtons SPNOpenMap"}).find('a').text

        #Smyths
        urlSmyths = 'https://www.smythstoys.com/ie/en-ie/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259'
        content = requests.get(urlSmyths)
        soup = bs.BeautifulSoup(content.text, 'lxml')
        stockSmyths = str(soup.find("form", {"id": "customAddToCartForm"}).find('button'))
        if stockGS == 'Out Of Stock':
            print('GS Out Of Stock\n')

        else:
            winner = 1
            embed = discord.Embed(
                title = 'PS5 IN STOCK',
                url = urlGS,
                color=discord.Color.green(),
                timestamp=datetime.datetime.now(tz=None)
            )
            embed.add_field(name='Type', value='Restock', inline=True)
            embed.add_field(name='Site', value='Gamestop IE', inline=True)
            embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png'),
            embed.set_thumbnail(url=imgURL)
            await ctx.send(embed=embed)
            await ctx.channel.send('<@&800002604381503518>')
            time.sleep(30)
            winner = 0

        if stockSmyths[53:66] == 'js-enable-btn':
            winner = 1
            embed = discord.Embed(
                title = 'PS5 IN STOCK',
                url = urlSmyths,
                color=discord.Color.red(),
                timestamp=datetime.datetime.now(tz=None)
            )
            embed.add_field(name='Type', value='Restock', inline=True)
            embed.add_field(name='Site', value='Smyths IE', inline=True)
            embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png'),
            embed.set_thumbnail(url=imgURL)
            await ctx.send(embed=embed)
            await ctx.channel.send('<@&800002604381503518>')
            time.sleep(30)
            winner = 0

        else:
            print('Smyths Out of Stock\n')

            
        if winner == 1:
            break
        time.sleep(3)

client.run(TOKEN)
