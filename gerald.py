import discord
import random
from discord.ext import commands, tasks

flipACoin = ["heads", "tails"]
eightball = ["yes", "no", "maybe", "that was a stupid question bitch", "YES YES YES", "gerald says no.", "ask later",
             "ask jaymel bruh", "honestly i dont even know", "sure?", "please never ask that question again.",
             "maybe maybe not"]
ppResponses = ["damn bro your cock is HOT", "mmm i dont know about that one bro",
               "step up your grindset dawg, your cock could use some work", "you're on the right track buddy, "
                                                                            "keep working on your cock",
               "ayo i dont know about that one, your cock is kinda weird", "holy shit your cock is a blessing "
                                                                           "from the gods",
               "mmmmmmm thats a nice cock :weary:", "shut it with your cock rating, its time for the taste test",
               "yo, can i get a closer look at that? :flushed:", "disgusting.", "that is a perfect cock. amazing"
                                                                                " length, balls, and amazingly clean",
               "No."]

token = 'ODY1MzM3MTc5NDAzNDUyNDcw.YPCiDA.e6SK0FEWzsrwxDHtTBomiTwwDyg'
bot = commands.Bot(command_prefix='gerald')

bot.remove_command("help")

# starting up the bot


@bot.event
async def on_ready():
    change_status.start()
    print("gerald running")
    await bot.change_presence(activity=discord.Game('ethan sus'))

# gerald responses


@bot.event
async def on_message(message):
    if message.content.startswith('hi'):
        await message.channel.send('hello')

    if message.content.startswith('sussy'):
        await message.channel.send('balls')

    if message.content.startswith('cocoa puffs'):
        await message.channel.send('cocoa nuts')

    if message.content.startswith('piss'):
        await message.channel.send('baby')

    if message.content.startswith('doing'):
        await message.channel.send('YOUR MOM')

    if message.content.startswith('photos printed'):
        await message.channel.send('bogos binted :alien:')

    if message.content.startswith('among'):
        await message.channel.send('us')

    if message.content.startswith('server link?'):
        await message.channel.send('here you go: https://discord.gg/mG2HT9Gy2J')

    if message.content.startswith('who is the impostor?'):
        await message.channel.send('You.')

    if message.content.startswith('bye'):
        await message.channel.send('later nerd')

    if message.content.startswith('whatchu'):
        await message.channel.send('know about rollin down in the deep')

    if message.content.startswith('we cock'):
        await message.channel.send('dick, ballin')

    if message.content.startswith('philip'):
        await message.channel.send('bruh')

    if message.content.startswith('hotel'):
        await message.channel.send('trivago')

    if message.content.startswith('when the'):
        await message.channel.send('impostor is sus :flushed:')

    if message.content.startswith('arbys'):
        await message.channel.send('we have the meats')

    if message.content.startswith('jaymel'):
        await message.channel.send('jaymel is very awesome')

    if message.content.startswith('hello gerald'):
        await message.channel.send("hello, " + message.author.mention)

    if message.content.startswith('Hello gerald'):
        await message.channel.send("hello, " + message.author.mention)

    if message.content.startswith('hello Gerald'):
        await message.channel.send("hello, " + message.author.mention)

    if message.content.startswith('flip a coin'):
        await message.channel.send(random.choice(flipACoin))

    if message.content.startswith('8ball'):
        await message.channel.send(random.choice(eightball))

    if message.content.startswith('cock rate'):
        await message.channel.send(random.choice(ppResponses))

    if message.content.startswith('bad song'):
        await message.channel.send("https://www.youtube.com/watch?v=lx-__lBS6a4")

    if message.content.startswith('good song'):
        await message.channel.send("https://www.youtube.com/watch?v=YeQGPbGJa4g&t=1s")

    if message.content.startswith('we do some trollin'):
        await message.channel.send('https://i.kym-cdn.com/photos/images/masonry/002/052/328/fdd.gif')

    if message.content.startswith('random number'):
        n = random.randint(0, 100)
        await message.channel.send(n)

    if message.content.startswith('stupid rate'):
        n = random.randint(0, 100)
        n_as_string = str(n)
        stupidrating = "you are " + n_as_string + "% stupid"
        await message.channel.send(stupidrating)

    if message.content.startswith('roll a dice'):
        n = random.randint(1, 6)
        await message.channel.send(n)


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="bruh", description="bruhhuh")

    await ctx.send(embed=em)


@help.command()
async def helping(ctx):
    em = discord.Embed(title="brah", description="brahhshh")
    await ctx.send(embed=em)

# gerald saying a certain message every hour


@tasks.loop(seconds=3600)
async def change_status():
    channel = bot.get_channel(866395882671964181)  # change this id to whatever channel
    # await channel.send('balls')  # change this to whatever you want the message to be

bot.run(token)
