"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("┈┈┈┈╱▔▔▔▔▔▔╲┈╭━━━╮┈┈┈ \n"
                     "┈┈┈▕┈╭━╮╭━╮┈▏┃BOO…┃┈┈┈ \n"
                     "┈┈┈▕┈┃╭╯╰╮┃┈▏╰┳━━╯┈┈┈ \n"
                     "┈┈┈▕┈╰╯╭╮╰╯┈▏┈┃┈┈┈┈┈┈ \n"
                     "┈┈┈▕┈┈┈┃┃┈┈┈▏━╯┈┈┈┈┈┈ \n"
                     "┈┈┈▕┈┈┈╰╯┈┈┈▏┈┈┈┈┈┈┈┈ \n"
                     "┈┈┈▕╱╲╱╲╱╲╱╲▏┈┈┈┈┈┈┈┈ \n\n"
                     "♠️♠️Kraken here♠️♠️ \n"
                     "================= \n"
                     "▲▲▲▲▲▲▲▲▲▲ \n"
                     "🄸   🄰🄼   🄰🄻🄸🅅🄴 \n"
                    "▼▼▼▼▼▼▼▼▼▼ \n"
                     "================= \n"
                     "Creation of sir @Kraken_op  \n"
                     "---------------------------------- \n"
                     "Maintainer:- кяαкєη")
