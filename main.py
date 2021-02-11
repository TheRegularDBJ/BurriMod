import discord
import os
#from webserver import keep_alive // para repl.it
from discord.ext import commands
from AntiSpam import AntiSpamHandler

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot=commands.Bot(command_prefix="%", intents=intents)
bot.remove_command('help')
warn_embed_dict = {
    "title": "**$USERNAME DEJA DE SPAMEAR**",
    "description": "has sido advertido por spam, por favor detente!",
    "timestamp": False,
    "color": 0x7289da,
    "fields": [
        {"name": "advertencias:", "value": "$WARNCOUNT", "inline": False},
        {"name": "expulsiones totales:", "value": "$KICKCOUNT", "inline": False},
    ],
}
bot.handler = AntiSpamHandler(bot, 1, ignore_bots=True, ban_threshold=1, guild_warn_message=warn_embed_dict, guild_kick_message="$USERNAME ha sido expulsado por spamear mucho", user_kick_message="$USERNAME, has sido expulsado de $GUILDNAME por spamear mucho", guild_ban_message="$USERNAME fue baneado por spamear mucho", user_ban_message="$USERNAME has sido baneado de los kabros por spamear mucho")

@bot.listen()
async def on_message(msg):
    bot.handler.propagate(msg)
    social = ["https://youtube.com/channel", "https://youtube.com/c", "https://youtu.be", "https://www.twitch.tv/", "https://www.youtube.com/channel", "https://www.youtube.com/c", "https://www.youtu.be", "https://reddit.com/u", "https://www.reddit.com/u", "https://twitch.tv/", "https://twitter.com/", "https://www.twitter.com/", "https://www.instagram.com", "https://instagram.com", "https://web.facebook.com", "facebook.com""https://discord.com/invite", "https://discord.gg/", "https://www.discord.com/invite", "www.discord.gg", "discord.gg"]
    for word in social:
        if msg.content.count(word) > 0:
            await msg.channel.purge(limit=1)
            #await msg.ban(reason="spammer_promotion", delete_message_days=1)
            await msg.author.send(f"oye! {msg.author.mention} las promociones estan prohibidas")
    await bot.process_commands(msg)


#keep_alive() //esta lineas son para repl.it
#BOT_TOKEN = os.environ.get("DISCORD_BOT_SECRET") //esta linea es para repl.it
#bot.run(BOT_TOKEN)
bot.run(token de tu bot)
