import discord
import random

# Configura el token de tu bot de Discord
DISCORD_BOT_TOKEN = 'Token'  # Reemplaza con el token de tu bot de Discord

# Lista de chistes predefinidos
chistes = [
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Por qué los programadores prefieren el verano? Porque hay menos bugs.",
    "¿Cuál es el colmo de un electricista? No encontrar corriente en su vida.",
    "¿Qué le dijo una impresora a otra? ¿Esa hoja es tuya o es una impresión mía?",
    "¿Cómo se dice pañuelo en japonés? Saka-moko.",
    "¿Por qué las focas miran siempre hacia arriba? ¡Porque ahí están los focos!",
    "¿Qué le dice un gusano a otro gusano? Voy a dar una vuelta a la manzana.",
    "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Por qué los pájaros no usan computadoras? Porque temen a los gusanos.",
    "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
    "¿Qué hace una abeja en el teléfono? ¡Zumbando!",
    "¿Qué hace un pez mago? Nada por aquí, nada por allá.",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Por qué los elefantes no usan computadoras? Porque le tienen miedo al ratón.",
    "¿Qué hace una abeja en la computadora? ¡Zumbando en Internet!",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Qué le dice un gusano a otro gusano? ¡Voy a dar una vuelta a la manzana!",
    "¿Qué hace un pez en el mar? Nada."
]

# Configura el cliente de Discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user} conectado y listo para contar chistes!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!chiste':
        chiste = random.choice(chistes)
        await message.channel.send(chiste)

client.run("TOKEN")
