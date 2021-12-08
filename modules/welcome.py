import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"<b>Hello {message.from_user.mention} 🙂</b>\n\n<b>Welcome to {message.chat.title} ,  Happy to see you</b>",chat_id=chatid)
    try:
        await bot.send_message.delete()

        
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"<b>Bye ,  {message.from_user.mention} , Have a Nice Day</b>",chat_id=chatid)
        



