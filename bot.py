import discord
import asyncio
import os

bot = discord.Client()

@bot.event
async def on_ready():
    '''print('Welcome to the BonPon Console. To list all the commands, type "help"')
    while True:
        cmd = str(input('BonPon>'))
        cmd = cmd.lower()
        if(cmd == 'help'):
            print('help :: Display help for the console \nexit :: Exits this program')
        elif(cmd == 'exit'):
            print('Bye Bye!')
            exit(0)'''


@bot.event
async def on_message(msg):
    prefix = 'p!';
    if msg.content.startswith(prefix) == False:
        return
    args = msg.content[2:].split(' ');
    command = args[0]
    args = args[1:]
    bot.send_typing(msg.channel)
    if(command == 'ping'):
        m = bot.send_message(msg.channel, 'If you see this, the bot is lagging')
        em = discord.Embed(title='PONG!', colour=0x00afff)
        em.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
        time = str(m.timestamp)
        em.add_field(name='Bot Latency (Client)', value=time + ' ms', inline=True)
        bot.delete_message(m)
        await bot.send_message(msg.channel, embed=em )
bot.run(os.environ['TOKEN'])
