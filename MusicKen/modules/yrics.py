import io
import os

from pyrogram import filters
from tswift import Song

from pyrogram import Client as pbot




# Lel, Didn't Get Time To Make New One So Used Plugin Made br @mrconfused and @sandy1709 dont edit credits


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("🔎 **Sedang Mencari lyrics**")
    query = message.text
    if not query:
        await lel.edit("**lyrics Tidak ditemukan**")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "**Tidak dapat menemukan lirik untuk lagu itu!** coba cari dengan judul lagu yang lebih jelas jika masih tidak berhasil coba `.glyrics`"
    else:
        reply = "**lyrics Tidak ditemukan** coba cari dengan judul lagu yang lebih jelas jika masih tidak berhasil coba `.glyrics`"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply
