from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PBXMUSIC import app
from PBXMUSIC.core.call import PBX
from PBXMUSIC.utils import bot_sys_stats
from PBXMUSIC.utils.decorators.language import language
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PBXMUSIC import app
from pyrogram import filters


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    PING_IMG_URL = "https://telegra.ph/file/7bb907999ea7156227283.jpg"
    captionss = "**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ.**"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionss))
    await asyncio.sleep(1)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ...**")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ.**")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ..**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ...**")
    await asyncio.sleep(2)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ....**")
    await asyncio.sleep(2)
    await response.edit_caption("**📡sʏsᴛᴇᴍ ᴅᴀᴛᴀ ᴀɴᴀʟʏsᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !**")
    await asyncio.sleep(3)
    await response.edit_caption("**📩sᴇɴᴅɪɴɢ sʏsᴛᴇᴍ ᴀɴᴀʟʏsᴇᴅ ᴅᴀᴛᴀ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    start = datetime.now()
    pytgping = await PBX.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text = _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    captions = "**ㅤ  🏓 ᴘɪɴɢ...ᴘᴏɴɢ...ᴘɪɴɢ✨\nㅤ  🎸 ʙᴀᴅ...ʙᴀᴅ...ʙᴀʙʏ💞**"
    await message.reply_photo(
        (carbon),
        caption=captions,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["S_B_5"],
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="✦ ɢʀᴏᴜᴘ ✦",
                        url=f"https://t.me/ll_Bot_Promotion_ll",
                    ),
                    InlineKeyboardButton(
                        text="✧ ᴍᴏʀᴇ ✧",
                        url=f"https://t.me/ll_OYE_KUNAAL_ll",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="❅ ʜᴇʟᴘ ❅", callback_data="settings_back_helper"
                    )
                ],
            ]
        ),
    )
    await response.delete()
