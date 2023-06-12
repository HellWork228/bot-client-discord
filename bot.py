import discord
from random_1 import gen_pass
from monetkap import flip_coin
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!паника'):
        await message.channel.send("ребят, давайте без паники, пожалуйста!")
    elif message.content.startswith('!привет'):
        await message.channel.send("Привет, я чат-бот panika! \nЯ могу много чего, можешь это узнать командой: \n!!panika")
    elif message.content.startswith('!сгенерируй случайное число от 0 до 10'):
        await message.channel.send(gen_pass(1))
    elif message.content.startswith('!монетка'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('!panika'):
        await message.channel.send("Ты попал в раздел правил!")
    else:
        await message.channel.send(message.content)

def new_func():
    return 1

client.run("токен")
