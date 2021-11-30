from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

APPER="mrc_venom"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('😌 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿', url='https://t.me/MrC_VENOM'),
                    InlineKeyboardButton('Group 😎', url='https://t.me/tvseriezzz')
                ],
                [
                    InlineKeyboardButton('Search Inline', switch_inline_query_current_chat='')
            ]
          ]
        ),
        reply_to_message_id=message.message_id
    )


@Client.on_message(filters.text)
def a(client, message):
    query =message.text
    print(query)
    m = message.reply('`🔎 𝗦𝗲𝗮𝗿𝗰𝗵𝗶𝗻𝗴 𝘁𝗵𝗲 𝗦𝗼𝗻𝗴.... 😌`')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 7000:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[𝕸𝖚𝖘𝖎𝖈]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=False)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('𝐅𝐨𝐮𝐧𝐝 𝐍𝐨𝐭𝐡𝐢𝐧𝐠. 𝐓𝐫𝐲 𝐂𝐡𝐚𝐧𝐠𝐢𝐧𝐠 𝐓𝐡𝐞 𝐒𝐩𝐞𝐥𝐥𝐢𝐧𝐠 𝐀 𝐋𝐢𝐭𝐭𝐥𝐞 😐...`')
            return
    except Exception as e:
        m.edit(
            "❎ 𝐹𝑜𝑢𝑛𝑑 𝑁𝑜𝑡ℎ𝑖𝑛𝑔. 𝐒𝐨𝐫𝐫𝐲.\n\n𝖯𝗅𝖾𝖺𝗌𝖾 𝖳𝗋𝗒 𝖠𝗀𝖺𝗂𝗇 𝖮𝗋 𝖲𝖾𝖺𝗋𝖼𝗁 𝖺𝗍 Google.com 𝖥𝗈𝗋 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 𝗈𝖿 𝗍𝗁𝖾 𝙎𝙤𝙣𝙜.\n\nEg.` Believer ´"
        )
        print(str(e))
        return
    m.edit("`Uploading Your File,Please Wait for Some Seconds...`[🎧](https://te.legra.ph/file/c3dce12116a0a8af80c93.jpg)")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎧 𝗧𝗶𝘁𝘁𝗹𝗲 : <a href="{link}">{title}</a>\n⏳ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻 : {duration}\n👀 𝗩𝗶𝗲𝘄𝘀 : {views}\n\n📮 𝗕𝘆: {message.from_user.mention()}\n<b>📤 𝗕𝘆 :- <a href="https://t.me/tvseriezzz_music">𝑨𝒍𝒍 𝑰𝒏 𝑶𝒏𝒆 𝑮𝒓𝒐𝒖𝒑 𝕸𝖚𝖘𝖎𝖈</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
        message.delete()
    except Exception as e:
        m.edit('**An internal Error Occured, Report This @MrC_VENOM_2!!**[🙂](https://te.legra.ph/file/c3dce12116a0a8af80c93.jpg)')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
