import discord
from discord.ext import commands
from settings import settings
import random
import requests
import numpy as np

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def remove(ctx, left: int, right: int):
    """removes two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def multiplicate(ctx, left: int, right: int):
    """multiplicate two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left: int, right: int):
    """divide two numbers together."""
    await ctx.send(left / right)

    if left == 0 or right == 0:
        print('ERROR 1507: division entre 0 detectada')

@bot.command()
async def raiz(ctx,n1:int):
    """Esta función suma dos números enteros y devuelve el resultado."""
    resultado2 = np.sqrt(n1)
    await ctx.send(f"La raiz cuadrada de {n1} {resultado2}")

@bot.command()
async def exp(ctx,n1:int, n2: int):
    resultado_exp = n1**n2
    await ctx.send(f"el numero {n1} elevado a la {n2} es {resultado_exp}")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def contaminacion_ambiental(ctx):
    await ctx.send(f"""Hola, soy {bot.user}, tu bot de confianza!""")
    await ctx.send(f'¿deseas saber un poco sobre la contaminacion ambiental?   "si" o "no" ')
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("La contaminacion ambiental es peligrosa, ya que esta dañando nuestros ecosistemas, algunos tipos de contaminacion ambiental son:")
            await ctx.send("1. acuatica: hay personas y fabricas que tiran sus desechos a los rios, mares o lagos lo cual provoca que el agua poco a poco se vuelva totalmente sucia si este problema continua no habra mas agua potable")   
            await ctx.send("2. aerea: los vehiculos que usan gasolina contaminan el aire provocando que la atmosfera se deteriore poco a poco, haciendo que los rayos solare golpeen la tierra más directamente")
            await ctx.send("3. terrestre: los desechos humanos como plastico, baterias y otros, contaminan el suelo y cuestan mucho de deshacerse por lo que se acumulan")
            await ctx.send("4. caza ilegal o furtiva: muchos animales como los pandas, ajolotes, pez gato, tiburon martillo, entre otros, se encuentran en peligro de extincion ya que quedan muy pocos de su especie")
        else:
            await ctx.send("comprendo, si alguna vez tienes una duda, no dudes en preguntarmelo.")
    else:
        await ctx.send("No te comprendo. ¿Me lo puedes repetir?")

@bot.command()
async def mem(ctx):
    meme = random.randint(1, 10)
    if meme == 1:
        with open('img/001.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 2:
        with open('img/002.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 3:
        with open('img/003.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 4:
        with open('img/004.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 5:
        with open('img/005.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 6:
        with open('img/006.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 7:
        with open('img/007.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 8:
        with open('img/008.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 9:
        with open('img/momazo.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)
    elif meme == 10:
        with open('img/momazo 2.jpg', 'rb') as f:
            # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run(settings['TOKEN'])

