# Credits: @mrismanaziz

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot <b>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]
