import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"<b>Welcome {message.from_user.mention} to {message.chat.title} ,  Happy to have here</b>",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📃 MUST READ | Click Here 📃", url="https://t.me/vayichitt_poyamathii")
                        ],
                        [
                            InlineKeyboardButton("🔍 Click Here & Go To Google 🔎", url="https://www.google.com")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"</b>Bye ,  {message.from_user.mention} , Have a Nice Day</b>",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📃 MUST READ | Click Here 📃", url="https://t.me/vayichitt_poyamathii")
                        ],
                        [
                            InlineKeyboardButton("🔍 Click Here & Go To Google 🔎", url="https://www.google.com")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )

	

