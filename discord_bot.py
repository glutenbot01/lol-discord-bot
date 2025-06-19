import discord
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    print("Warning: Discord token not found in environment variables!")
    exit(1)

# Full champion pools by role (as of Jan 2025; 170 total)
champions_by_role = {
    "Top": [
        "Aatrox","Camille","Cho’Gath","Darius","Dr. Mundo","Fiora","Gangplank","Garen",
        "Gnar","Gragas","Gwen","Heimerdinger","Illaoi","Irelia","Jax","Jayce","K’Sante",
        "Kennen","Kled","Malphite","Mordekaiser","Nasus","Ornn","Poppy","Quinn","Renekton",
        "Riven","Rumble","Shen","Singed","Sion","Teemo","Trundle","Tryndamere","Urgot",
        "Vladimir","Wukong","Yorick","Sett","Maokai","Cho’Gath","Heimerdinger","Quinn","Poppy","Gangplank"
    ],
    "Jungle": [
        "Amumu","Bel’Veth","Elise","Ekko","Evelynn","Fiddlesticks","Graves","Gragas","Hecarim",
        "Ivern","Jarvan IV","Kayn","Kha’Zix","Kindred","Lee Sin","Lillia","Master Yi","Nidalee",
        "Nunu & Willump","Olaf","Rammus","Rek’Sai","Rengar","Sejuani","Shaco","Shyvana","Udyr",
        "Vi","Volibear","Warwick","Xin Zhao","Zac","Karthus","Naafiri"
    ],
    "Mid": [
        "Ahri","Akali","Anivia","Annie","Aurelion Sol","Azir","Brand","Cassiopeia","Corki",
        "Diana","Fizz","Galio","Kassadin","Katarina","LeBlanc","Lissandra","Malzahar","Morgana",
        "Neeko","Orianna","Qiyana","Ryze","Samira","Seraphine","Syndra","Swain","Taliyah",
        "Talon","Twisted Fate","Veigar","Vel’Koz","Viktor","Vex","Xerath","Zed","Ziggs",
        "Yasuo","Yone","Aurora","Mel"
    ],
    "ADC": [
        "Akshan","Aphelios","Ashe","Caitlyn","Draven","Ezreal","Jhin","Jinx","Kai’Sa",
        "Kalista","Kog’Maw","Lucian","Miss Fortune","Sivir","Tristana","Twitch","Varus",
        "Vayne","Xayah","Zeri","Nilah","Smolder"
    ],
    "Support": [
        "Alistar","Bard","Blitzcrank","Braum","Janna","Karma","Leona","Lulu","Nami",
        "Nautilus","Pyke","Rakan","Renata Glasc","Rell","Seraphine","Senna","Sona","Soraka",
        "Taric","Thresh","Zilean","Zyra","Yuumi","Milio"
    ],
}

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is online and ready to randomize!")

@client.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from any bot, including itself

    # Debug print to check for duplicates (optional)
    # print(f"Received message: {message.content} from {message.author} in {message.channel}")

    if message.content.lower().startswith("!team"):
        comp = { role: random.choice(champs) for role, champs in champions_by_role.items() }
        resp = "**🎮 Random League Team Comp:**\n"
        for role, champ in comp.items():
            resp += f"**{role}:** {champ}\n"
        await message.channel.send(resp)

client.run(TOKEN)


