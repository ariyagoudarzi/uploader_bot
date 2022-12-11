from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Command For User BOT
 ├ /start - Starting Bot
 ├ /about - About This Bot
 ├ /help - helpers 
 ├ /ping - check alive
 └ /uptime - see status bot 
 
 ❏ Command For Admin BOT
 ├ /logs - see logs bot
 ├ /setvar - setup var with command dibot
 ├ /delvar - delete var with command dibot
 ├ /getvar - see vars with command dibot
 ├ /users - see stats user
 ├ /batch - create link with multifile
 ├ /speedtest - check speed server bot
 └ /broadcast - broadcasting 

👨‍💻 Develoved by @hdiiofficial
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About This Bot:

@{} is Bot Telegram for keep file and can acces with special link 

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>

👨‍💻 Develoved by @hdiiofficial
"""
