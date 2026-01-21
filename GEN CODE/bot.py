import os
import asyncio
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix = ['g ','G','Gen','gen'], help_command = None, intents = intents)
client.remove_command('help')

bite_images = [
"https://tenor.com/view/milk-and-mocha-bears-clingy-notice-me-heart-gif-13418531",
"https://tenor.com/view/mochi-mochi-peach-cat-bite-head-cute-cats-bite-gif-17946884",
"https://tenor.com/view/milk-and-mocha-bite-wake-up-gnam-gif-11674205",
]

hug_images = [
"https://tenor.com/view/ilove-you-chris-gif-18073591",
"https://tenor.com/view/hugmati-gif-18302861",
"https://tenor.com/view/milk-and-mocha-hug-cute-kawaii-love-gif-12535134",
"https://tenor.com/view/milk-and-mocha-hug-cute-kawaii-love-gif-12535134",
]

handholding_images = [
"https://tenor.com/view/sleeping-together-cute-holding-hands-moving-ears-gif-17331664",
"https://tenor.com/view/mimineko-anh-thien-be-heo-yeah-walking-hold-hands-gif-17731735",
]

kiss_images = [
"https://tenor.com/view/milkandmocha-kissing-love-gif-13123974",
"https://tenor.com/view/milk-and-mocha-bear-couple-kisses-kiss-love-gif-12498627",
"https://tenor.com/view/kisses-love-couple-kiss-muah-gif-16851922",
]

blush_images = [
"https://tenor.com/view/milk-and-mocha-bear-couple-aww-thanks-blush-gif-12498619",
"https://tenor.com/view/excited-milk-and-mocha-cute-bear-white-bear-love-bear-gif-15248522",
"https://tenor.com/view/skunk-shy-blushing-cute-cartoon-gif-4817352",
]

punch_images = [
"https://tenor.com/view/face-punch-punch-minions-fine-happy-gif-4902917",
"https://tenor.com/view/lulugifs-charlie-brown-lucy-peanuts-punch-gif-15768734",
"https://tenor.com/view/brown-cony-sorry-punch-gif-13627939",
"https://tenor.com/view/boxing-box-punch-hit-fight-gif-5393841",
]

slap_images = [
"https://tenor.com/view/spongebob-squarepants-patrick-star-gloves-slap-gif-17514643",
"https://tenor.com/view/slap-face-funny-family-guy-stewie-griffin-gif-15003911",
"https://tenor.com/view/baka-slap-huh-angry-gif-15696850",
"https://tenor.com/view/bobs-burgers-louise-louise-slaps-slap-gif-12656044",
"https://tenor.com/view/slap-handaseishuu-narukotoishi-barakamonanime-barakamon-gif-5509136",
]

@client.event
async def on_ready():
    print("bot is ready.")

#import pdb; pdb.set_trace()

@client.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="Gen's Help Center!")
    command_names_list = [x.name for x in client.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(client.commands)]),
            inline=False
        )

        help_embed.add_field(
            name="Details",
            value="Type in ` g help <command name>` and i'll tell you more about the command.",
            inline=False
        )
    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=client.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="uhm.... ",
            value="I don't have that command..."
        )
    await ctx.send(embed=help_embed)

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'wow...{member} has left the server.')

@client.command()
async def ping(ctx, help="see how fast I'm running "):
    await ctx.send(f'Pong!{round(client.latency*1000)}ms')

@client.command()
async def punch(ctx, help = "sends a punching gif"):
    await ctx.send(random.choice(punch_images))

@client.command(aliases = ["8ball","test"])
async def _8ball(ctx, *, question, help="see a glimpse into your future with the magical 8 ball "):
    responses = ['It is most certain',
        'There was never a chance',
        'possibly',
        'try again later',
        'It is certain',
        'Do you really need me to answer that?',
        'Most likely',
        'Not likely',
        'It is definite',
        'No',
        'Yes',
            ]
    await ctx.send(f'question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def slap(ctx):
    await ctx.send(random.choice(slap_images))

@client.command()
async def hug(ctx):
    await ctx.send(random.choice(slap_images))


@client.command()
async def HH(ctx):
    await ctx.send(random.choice(handholding_images))


@client.command()
async def bite(ctx):
    await ctx.send(random.choice(bite_images))


@client.command()
async def kiss(ctx):
    await ctx.send(random.choice(kiss_images))

@client.command()
async def blush_images(ctx):
    await ctx.send(random.choice(blush_images))

@client.command()
async def debby(ctx):
    await ctx.send("https://tenor.com/view/debby-ryan-fix-hair-smile-pretty-sassy-gif-17073489")




@client.command()
async def rps(ctx, help="play a totally fair and fun game of rock, paper, scissors with a completely beatable AI"):
    await ctx.send('Rock, paper, scissors, shoot!')

    bot_choice = random.choice(['rock', 'paper', 'scissors'])

    try:
        player_choice = await client.wait_for('message', timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you took too long it was {bot_choice}.')

    await ctx.send(f" the my choice was {bot_choice}.")
    if bot_choice == "rock" and player_choice == "scissors":
        await ctx.send('bot won!')
    elif bot_choice == "rock" and player_choice == "paper":
        await ctx.send("player won!")
    elif bot_choice == "paper" and player_choice == "scissors":
        await ctx.send("player won!")
    else:
        await ctx.send("Ha! I win!")
        #make this more interactive where if user inputs "rock" and the bot chooses scissors than a message saying "you win" appears.

#@client.command()
#async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
#    slapped = ", ".join(x.name for x in members)
#    await ctx.send('{} just got slapped for {}'.format(slapped, reason))



client.run(os.getenv("DISCORD_TOKEN"))


#ODMyNDc4MDM0ODI4ODUzMjU3.YHkXlg.4Y1zlO-85QoGM8XgFlH4rJauS4k


#import pdb; pdb.set_trace()

#def generate_response(user_input):
  #responses = [
    #"oooo nice",
    #"You don't say!",
    #"Very cool!",
    #"I like that"
  #]
  #return random.choice(responses)
#find a way to add this to my code^^^

    # emoji = '\N{THUMBS UP SIGN}'
# or '\U0001f44d' or '👍'
#await message.add_reaction(emoji)
