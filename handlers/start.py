from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""🙃 Hi {message.from_user.first_name}!
↗↖GUA ADALAH SATRIA JEMBOT HITAM. 
🥳 ADA YANG BISA SAYA BANTAI? EH BANTU MANGSUDNYA
⚜️ GUNAKAN TOLOL DIBAWAH INI !! RALAT MANGSUDNYA ITU TOMBOL HEHE""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source code", url="https://www.xnxx.com"
                    )
                    
                    
                    InlineKeyboardButton(
                        "⚒ Source code", url="https://www.xvideos.com"
                    )
                
                  
                 
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "**Hêllẞø†:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
