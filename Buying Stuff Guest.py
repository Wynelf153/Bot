import discord      # pip3 install discord.py
import asyncio
import time
from discord.ext import commands
from os import path

#Gwyn-Bot

count1 = 1000
count2 = 1000
count3 = 0
count4 = 0
count5 = 0
ID = 0
convenient = 0
accept = 0
start = 0
stage = 0
page = 0
index1 = 0
index2 = 0
nopages = 0
marketno = ''
marketlist = ''
price = ''
server = ''
commandf = ''
commandb = ''
user = [
'326656614516129792',
'458120975825764366',
'404898624603029505',
'351912505561448448',
'439897741703905300'
]
TOKEN = "NDM5ODk3NzQxNzAzOTA1MzAw.Dt2hmw.IA0G0QPiNRGiZV9Ap-MeRVjIJyg"
pokemonlist = {}
bot = commands.Bot(command_prefix="%%", description='''Selfbot by Godwyn''', self_bot=True)

@bot.event
async def on_message(message):
    global count1
    global count2
    global count3
    global count4
    global count5
    global index1
    global index2
    global nopages
    global marketno
    global marketlist
    global convenient
    global accept
    global start
    global stage
    global page
    global price
    global server
    global commandf
    global commandb
    global user
    
    if (message.content.startswith('analyze')
    and str(message.author.id) in user
        ):
        count4 = 0
        try:
            accept =(str(message.content)[8:])
            convenient = accept.find(' ') 
            accept = accept[:convenient]
            convenient = (str(message.content)).find(accept)+len(accept)+1
            nopages = (str(message.content))[convenient:]
            accept = float(accept)
        except ValueError:
            await message.channel.send('Oops... is that a number? Please enter a number.')
            return
        if nopages == ' ' or nopages == '':
            print("oops... can't find what nopages is.")
            print('nopages = ' + str(nopages))
            count5 = 0
            server = str(message.channel.id)
            return
        nopages = int(nopages)
        count5 = nopages
        server = str(message.channel.id)

    if (message.content.startswith('p!')
    and str(message.author.id) in user
    and str(message.channel.id) == server
    and stage != 1
        ):
        commandf = str(message.content)
        convenient = commandf.find('market search')
        commandb = commandf.find('--name')
        if (convenient == -1 or commandb == -1) and stage != 1:
            await message.channel.send("Oops, I don't know what to do...")
            return
        commandb = commandf[commandb-1:]
        commandf = commandf[:convenient+14]
        count1 = 0
        

    if (str(message.channel.id) == server
        ):
        count1 = count1 + 1

    if (str(message.author.id) == '365975655608745985'
        and message.embeds
        and count1 < 4
        and str(message.channel.id) == server
        ):
        emb = message.embeds[0]
        middle = emb.description
        bottom = str(emb.footer)
        convenient = bottom.find('Showing')+8
        if convenient == '-1':
            await message.channel.send("Oops... I don't know what to do...")
            return
        convenient = bottom.find('-')+1
        page = bottom[convenient:]
        convenient = page.find('of')
        page = float(page[:convenient])
        page = page/20
        for a in list(range(20)):
            convenient = middle.find('Price: ')
            if convenient == -1:
                await message.channel.send("Oops... I don't know what to do...")
                return
            price = middle[convenient+6:]
            middle = price
            convenient = price.find('Credits')
            middle = price[convenient:]
            price = float(price[:convenient])
            if float(price) > float(accept):
                return
        time.sleep(2)
        marketlist = emb.description
        stage = 1
        while count3 < 20:
            index1 = marketlist.find('| ID:')
            index2 = (marketlist[index1+6:]).find('|')
            marketno = (marketlist[(index1+6):index1 + index2+6])
            marketlist = marketlist[index1 + index2 + 26:]
            await message.channel.send('p!market buy ' + marketno)
            time.sleep(1.75)
            count3 = count3 + 1
            if float(int(count3/3)) == float(count3/3):
                await message.channel.send('p!confirmbuy')
                time.sleep(1.75)
            if int(count3) == 20:
                await message.channel.send('p!confirmbuy')
                time.sleep(5)
        stage = 0
        if count4 < count5:
            await message.channel.send(commandf + str(int(page)) + commandb)
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = count4 + 1
            return
        await message.channel.send("I'm done with buying, should I go on?")
        count1 = 0
        count2 = 0
        count3 = 0

    if (message.content.startswith('go')
    and str(message.author.id) in user
    and str(message.channel.id) == server
    and count2 < 4
        ):
        await message.channel.send(commandf + str(int(page)) + commandb)
        count4 = 0

    if (message.content.startswith('stop')
    and str(message.author.id) in user
    and str(message.channel.id) == server
        ):
        count4 = count5
        count3 = 21
        

        
@bot.event
async def on_ready():
    print('Market bot')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN, bot=False)
