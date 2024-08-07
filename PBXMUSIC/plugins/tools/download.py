import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from PBXMUSIC import app
from ... import *
from PBXMUSIC import userbot as us, app
from PBXMUSIC.core.userbot import assistants

# List of commands to handle
commands = ["l2"]

@app.on_message(filters.command(commands))
async def dnr(client: Client, message: Message):
    if len(message.text.split()) < 2 and not message.reply_to_message:
        return await message.reply("Usage: /<command> <link> or reply to a message with the link.")
    
    link = message.text.split()[1] if not message.reply_to_message else message.reply_to_message.text
    if not link:
        return await message.reply("Please provide a valid link.")
    
    response_message = await message.reply("Processing...")

    # Choose a userbot assistant
    if 1 in assistants:
        ubot = us.one
    else:
        return await response_message.edit("No available userbot assistants.")

    # Send the link to the bot
    target_bot = "@UVDownloaderBot"
    try:
        sent_message = await ubot.send_message(target_bot, link)
    except Exception as e:
        return await response_message.edit(f"Failed to send the link: {e}")

    await asyncio.sleep(5)  # Increased sleep to ensure the bot has time to process

    # Fetch the last received media after sending the link
    media_downloaded = False
    try:
        async for bot_response in ubot.search_messages(target_bot, limit=1):
            if bot_response.media:
                file_path = await ubot.download_media(bot_response)
                if file_path:
                    media_downloaded = True
                    await client.send_document(
                        chat_id=message.chat.id,
                        document=file_path
                    )
                    os.remove(file_path)  # Clean up downloaded file
                    break
        if not media_downloaded:
            await response_message.edit("No media found in the bot's response.")
    except Exception as e:
        await response_message.edit(f"Failed to download and upload the media: {e}")
        return

    await response_message.delete()
