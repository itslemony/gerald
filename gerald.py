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
               "No.", ":microscope:", "bro what the fuck where is it i cant even see it", "SMELLY ALERT :rotating"
                                                                                          "_light:",
               "stop. i dont wanna see that shit anymore."]
geraldhatred = [" I'm so unbelievably done with you. I truly cannot deal with your bullshit anymore and it's entirely "
                "your fault. You're too stupid to realize how lucky you are. Your situation is like a wet dream for "
                "every boy your age. Have you ever thought about how fortunate you are that a pretty high school girl "
                "even bothered to be on your level of existence? Are you just that idiotic? And what about me? Do you "
                "know how demoralizing it is to be ghosted and ignored by a fucking 8th grader? You are such a piece "
                "of "
                "shit 'WinWin'(and what the fuck kinda name is WinWin anyway?) Do you even think, like, at all? I bet "
                "you're an unpopular bitch in middle school and you spend half your time in class "
                "dreaming "
                "of being a footrest for some 5/10 with braces and glasses. Your personality is probably "
                "being rude to people and getting annoyed when they're upset and also having blue eyes. I gave you "
                "time "
                "out of my day and listened to your bullshit but the first time I call your fuckboy ass for anything "
                "besides you you ignore me. I can't help but feel like you're probably the biggest fucking piece of "
                "shit"
                " in your entire school. You're like bubble gum on the bottom of my shoe and the world would be better"
                " without you. Kys :heart:"]
randomFacts = ["Due to it's location on the San Andreas fault, California will soon split apart and parts of the state "
               "will fall into the ocean",
               "Listening to Ed Sheeran for a prolonged period of time can cause your lifespan to decrease",
               "Kevin Durant, one of the athletes on the Manchester City soccer team, has scored the most touchdowns "
               "in MLB history.", "Italy isn't real",
               "All people with red hair are secretly Markiplier. Similar to this, all people with light "
               "blue hair are secretly Ninja from Fortnite.", "Your penis is small.", "I had sex with your mom last "
               "night", "Australia is upside-down.", "The Earth is shaped like a pear.", "PEE IS IN THE BALLS"]
jokes = ['You.', 'Hey do you like Chef Boyardee? ||Chef Boy-Are-Deez nuts tasty :weary:||', 'What do you call a train '
         'that '
         'is carrying bubblegum? '
         '|| a chew-chew train'
         ' :smiling_imp: ||',
         'Look in the mirror.']
geraldEmotion = ["i'm doing pretty good, thanks for asking", "things could definitely be a lot better", "life is shit."
                 "not very good. jaymel is keeping me hostage.", "i'm tired", "im great, thanks", "i dont know anymore"
                 "help", "thank you for asking, im doing okay B)"]

songs = [r"C:\Users\April\Downloads\Wellerman.mp3", r"C:\Users\April\Downloads\God.mp3",
         r"C:\Users\April\Downloads\Sus.mp3"]

token = 'token'
bot = commands.Bot(command_prefix='gerald')


# starting up the bot


@bot.event
async def on_ready():
    change_status.start()
    print("gerald running")
    await bot.change_presence(activity=discord.Game('use "gerald help" to see my website and view commands'))


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

    if message.content.startswith('gerald server'):
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

    if message.content.startswith('hello gerald'):
        await message.channel.send("hello, " + message.author.mention)

    if message.content.startswith('Hello gerald'):
        await message.channel.send("hello, " + message.author.mention)

    if message.content.startswith('hello Gerald'):
        await message.channel.send("hello, " + message.author.mention)

    if message.content.startswith('gerald flip a coin'):
        await message.channel.send(random.choice(flipACoin))

    if message.content.startswith('gerald 8ball'):
        await message.channel.send(random.choice(eightball))

    if message.content.startswith('gerald cock rate'):
        await message.channel.send(random.choice(ppResponses))

    if message.content.startswith('how are you gerald'):
        await message.channel.send(random.choice(geraldEmotion))

    if message.content.startswith('gerald bad song'):
        await message.channel.send("https://www.youtube.com/watch?v=lx-__lBS6a4")

    if message.content.startswith('gerald good song'):
        await message.channel.send("https://www.youtube.com/watch?v=YeQGPbGJa4g&t=1s")

    if message.content.startswith('we do some trollin'):
        await message.channel.send('https://i.kym-cdn.com/photos/images/masonry/002/052/328/fdd.gif')

    if message.content.startswith('gerald random number'):
        n = random.randint(0, 100)
        await message.channel.send(n)

    if message.content.startswith('gerald stupid rate'):
        n = random.randint(0, 100)
        n_as_string = str(n)
        stupidrating = "you are " + n_as_string + "% stupid"
        await message.channel.send(stupidrating)

    if message.content.startswith('gerald help'):
        await message.channel.send('heres my website: https://geraldshrine.w3spaces.com/inde'
                                   'x.html?bypass-cache=1626657983')

    if message.content.startswith('gerald ping'):
        await message.channel.send(f'pong B) ({round(bot.latency * 1000)}ms)')

    if message.content.startswith('gerald account age'):
        user = message.author
        await message.channel.send(user.created_at)

    if message.content.startswith('thank you gerald'):
        await message.channel.send('ur welcome, ' + message.author.mention + '!')

    if message.content.startswith('thank you, gerald'):
        await message.channel.send('ur welcome, ' + message.author.mention + '!')

    if message.content.startswith('thanks gerald'):
        await message.channel.send('ur welcome, ' + message.author.mention + '!')

    if message.content.startswith('thanks. gerald'):
        await message.channel.send('ur welcome, ' + message.author.mention + '!')

    if message.content.startswith('i love u gerald'):
        elif message.author.id == 270104205472038912:
            await message.channel.send('fuck you dad')
        else:
            await message.channel.send('ayo??? :flushed:')

    if message.content.startswith('i love you gerald'):
        elif message.author.id == 270104205472038912:
            await message.channel.send('fuck you dad')
        else:
            await message.channel.send('ayo??? :flushed:')

    if message.content.startswith('i love u, gerald'):
        elif message.author.id == 270104205472038912:
            await message.channel.send('fuck you dad')
        else:
            await message.channel.send('ayo??? :flushed:')

    if message.content.startswith('i hate you gerald'):
        await message.channel.send(random.choice(geraldhatred))

    if message.content.startswith('I hate you gerald'):
        await message.channel.send(random.choice(geraldhatred))

    if message.content.startswith('i hate u gerald'):
        await message.channel.send(random.choice(geraldhatred))

    if message.content.startswith('i hate u, gerald'):
        await message.channel.send(random.choice(geraldhatred))

    if message.content.startswith('i hate you, gerald'):
        await message.channel.send(random.choice(geraldhatred))

    if message.content.startswith('you suck gerald'):
        await message.channel.send(
            'ok when robots figure out how to kill humans youll be the first one to go asshole :middle_finger:')

    if message.content.startswith('give me free nitro' or 'free nitro'):
        await message.channel.send('ok, you know what? you guys have been a great server. you deserve this. '
                                   'here you go! free nitro! <https://bit.ly/3ix8VHI>')

    if message.content.startswith('gerald fact'):
        await message.channel.send(random.choice(randomFacts))

    if message.content.startswith('gerald joke'):
        await message.channel.send(random.choice(jokes))

    if message.content.startswith('gerald join'):
        vc = message.author.voice.channel
        if vc:
            await vc.connect()
        else:
            await message.channel.send('you arent in a vc dingus')

    if message.content.startswith('gerald disconnect'):
        server = message.guild
        voice_client = server.voice_client
        await voice_client.disconnect()

    if message.content.startswith('gerald dc'):
        server = message.guild
        voice_client = server.voice_client
        await voice_client.disconnect()

    if message.content.startswith('gerald play me a song'):
        vc = await message.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=random.choice(songs)))
        await message.channel.send('now playing a very cool song B)')

# gerald saying a certain message every hour


@tasks.loop(seconds=3600)
async def change_status():
    channel = bot.get_channel(866395882671964181)  # change this id to whatever channel
    # await channel.send('balls')  # change this to whatever you want the message to be

bot.run(token)
