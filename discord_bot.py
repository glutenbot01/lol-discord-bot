import discord
import random
import os

# Load token from environment
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    print("❌ DISCORD_TOKEN not set in environment.")
    exit(1)

# Champion pools by role
champions_by_role = {
    "Top": [
        "Aatrox", "Camille", "Cho’Gath", "Darius", "Dr. Mundo", "Fiora", "Gangplank", "Garen",
        "Gnar", "Gragas", "Gwen", "Heimerdinger", "Illaoi", "Irelia", "Jax", "Jayce", "K’Sante",
        "Kennen", "Kled", "Malphite", "Mordekaiser", "Nasus", "Ornn", "Poppy", "Quinn", "Renekton",
        "Riven", "Rumble", "Shen", "Singed", "Sion", "Teemo", "Trundle", "Tryndamere", "Urgot",
        "Vladimir", "Wukong", "Yorick", "Sett", "Maokai"
    ],
    "Jungle": [
        "Amumu", "Bel’Veth", "Elise", "Ekko", "Evelynn", "Fiddlesticks", "Graves", "Gragas", "Hecarim",
        "Ivern", "Jarvan IV", "Kayn", "Kha’Zix", "Kindred", "Lee Sin", "Lillia", "Master Yi", "Nidalee",
        "Nunu & Willump", "Olaf", "Rammus", "Rek’Sai", "Rengar", "Sejuani", "Shaco", "Shyvana", "Udyr",
        "Vi", "Volibear", "Warwick", "Xin Zhao", "Zac", "Karthus", "Naafiri"
    ],
    "Mid": [
        "Ahri", "Akali", "Anivia", "Annie", "Aurelion Sol", "Azir", "Brand", "Cassiopeia", "Corki",
        "Diana", "Fizz", "Galio", "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Malzahar", "Morgana",
        "Neeko", "Orianna", "Qiyana", "Ryze", "Samira", "Seraphine", "Syndra", "Swain", "Taliyah",
        "Talon", "Twisted Fate", "Veigar", "Vel’Koz", "Viktor", "Vex", "Xerath", "Zed", "Ziggs",
        "Yasuo", "Yone", "Aurora", "Mel"
    ],
    "ADC": [
        "Akshan", "Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Jinx", "Kai’Sa",
        "Kalista", "Kog’Maw", "Lucian", "Miss Fortune", "Sivir", "Tristana", "Twitch", "Varus",
        "Vayne", "Xayah", "Zeri", "Nilah", "Smolder"
    ],
    "Support": [
        "Alistar", "Bard", "Blitzcrank", "Braum", "Janna", "Karma", "Leona", "Lulu", "Nami",
        "Nautilus", "Pyke", "Rakan", "Renata Glasc", "Rell", "Seraphine", "Senna", "Sona", "Soraka",
        "Taric", "Thresh", "Zilean", "Zyra", "Yuumi", "Milio"
    ],
}

# Set up bot with slash support
intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

# Notify when bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

# Slash command for team comp
@bot.slash_command(name="team", description="🎮 Generate a random League of Legends team composition")
async def team(ctx: discord.ApplicationContext):
    comp = {role: random.choice(champs) for role, champs in champions_by_role.items()}
    response = "**🎮 Random League Team Comp:**\n"
    for role, champ in comp.items():
        response += f"**{role}:** {champ}\n"
    await ctx.respond(response)

# Run the bot
bot.run(TOKEN)
