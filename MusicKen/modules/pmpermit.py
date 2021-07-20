from pyrogram import Client
import asyncio
from MusicKen.config import SUDO_USERS, PMPERMIT, OWNER, PROJECT_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from pyrogram import filters
from pyrogram.types import Message
from MusicKen.services.callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE" and PMSET:
        chat_id = message.chat.id
        if chat_id in pchats:
            return
        await USER.send_message(
            message.chat.id,
            f"""This is a music service of @LaguKamuBot\n┏━━━━━━━━━━━━━━━━━━━━━\n ✦҈͜͡➳ Not a place to chat.\n ✦҈͜͡➳ Don't spam in here.\n ✦҈͜͡➳ Don't share private info in here.\n┗━━━━━━━━━━━━━━━━━━━━━\n\nManaged by : @fhroziiiii"""
        )
        return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("**pmpermit dinyalakan**")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("**pmpermit dimatikan**")
            return

@USER.on_message(filters.text & filters.private & filters.me)
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("Disetujui untuk private message")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("yes", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id not in pchats:
        pchats.append(chat_id)
        await message.reply_text("Disetujui untuk private message")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("no", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Maaf anda ditolak untuk private message")
        return
    message.continue_propagation()    
