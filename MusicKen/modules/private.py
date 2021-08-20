import logging
from MusicKen.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicKen.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""ZENO MSC adalah layanan musik telegram yang memiliki fitur:
 × Memutar lagu di group 
 × Mendownload lagu
 × Mendownload video
 × Mencari link youtube
 × Mencari lirik lagu
 × Klik tombol bantuan untuk informasi lebih lanjut

🔓 izin owner untuk dapat menambahkan bot
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BANTUAN", callback_data = f"help+1")],
                [
                    InlineKeyboardButton(
                        "HUBUNGI OWNER", url=f"https://t.me/{SUPPORT_GROUP}")],
                [
                    InlineKeyboardButton(
                        "+ TAMBAHKAN KE GROUP", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]        
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""🔊 {PROJECT_NAME} telah aktif""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Music downloader", url=f"https://t.me/lagukamubot"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'next »', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton(text = '« previous', callback_data = f"help+1")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '« previous', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'next »', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""Layanan musik telegram.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Music downloader", url=f"https://t.me/lagukamubot"
                    )
                ]
            ]
        ),
    )

@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""🔊 Bot berhasil dimulai ulang!""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨🏻‍💻 Bot Owner", url=f"https://t.me/{OWNER}"
                    )
                ]
            ]
        )
   )

