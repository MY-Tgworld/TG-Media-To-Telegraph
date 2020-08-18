# This is bot coded by @Noob_admim and used for educational purposes only
# Copyright of all images uploaded by this bot is goes to respected owners

import os
from pyrogram import Client,Filters
from telegraph import upload_file

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>I'm a Telegram To Telegra.ph Image/Video Uploader Bot. \n Created By @noob_admin</b> \n  Do /help For More",
        reply_to_message_id=message.message_id
    )

@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b> Send Me Any Video Or Photo I'll Upload It Into Telegra.ph. \n Created By @noob_admin</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(Filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>Downloading</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>Uploading🙋</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @Noob_admin")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(Filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @Noob_admin")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

@Client.on_message(Filters.animation)
async def getanime(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    animdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".gif"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=animdir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(animdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @No_OnE_Kn0wS_Me")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(animdir)
    except:
        pass

@Client.on_message(Filters.text)
async def text(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>Please Don't Spam Here \n Send Me A Photo Or Video To Convert It In Telegra.ph Link \n \n Bot Created By : @Mai_bOTs </b>",
        reply_to_message_id=message.message_id
    )
