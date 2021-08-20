import os
from MusicKen.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
• /play (judul) : memutar lagu dari youtube
• /ytplay (judul) : memutar lagu tanpa memilih
• /current : menampilkan trek lagu
• /playlist : menampilkan daftar putar

• /skip : untuk ke lagu berikutnya
• /pause : untuk menunda pemutaran
• /resume : untuk melanjutkan pemutaran
• /end : untuk menghentikan pemutaran
""",

f"""
• /musicplayer (on/off) : aktifkan/nonaktifkan bot
• /admincache : memperbarui info admin grup
• /userbotjoin : mengundang asisten ke grup

• /song (judul) : unduh audio dari youtube
• /vsong (judul) : unduh video dari youtube
• /search (judul) : mencari lagu dari youtube
• /lyrics (judul) : untuk mendapatkan lirik lagu
"""
      ]
