
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""[👋](https://telegra.ph/file/0dd62ad35eb6209d4217d.jpg)
**مرحبا بك فـ سـوُرس ســافو يتيح لك تشغيل الموسيقي والفيديو بدون اي مشكله وبدون تهنيج 🤍😊
        
امـامـك الـبـوت الـخـاص بـنـا..♡ [𝙱𝙾𝚃 𝚂𝙰𝚅𝙾](https://t.me/B8stat_bot)
نـتـمنـي لـكـم الـاسـتـمـتـاع بـهـذا الـبـوت 😇**

💞  تم برمجة البوت بواسطة 

⋆  [سـافو](t.me/s_a_s_a_3li)
⋆  [عـازف](https://t.me/X_X_A_Z_F_X_X2)
⋆  [الامبراطور حسن](https://t.me/theemperorhb)
⋆  [◟المطـور سـافو](https://telegra.ph/file/0dd62ad35eb6209d4217d.jpg)
 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور البوت..♡", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "مـبرمج الـسورس..♡", url="https://t.me/s_a_s_a_3li"
                    ),
                    InlineKeyboardButton(
                        "الـاوامـر..♡", url="https://telegra.ph/%F0%9D%98%BE%F0%9D%99%A4%F0%9D%99%A2%F0%9D%99%A2%F0%9D%99%96%F0%9D%99%A3%F0%9D%99%99%F0%9D%99%A8-%F0%9D%99%81%F0%9D%99%A4%F0%9D%99%A7-%F0%9D%98%BD%F0%9D%99%A4%F0%9D%99%A9-%F0%9D%98%BF%F0%9D%99%AA%F0%9D%99%A3%F0%9D%99%9E%F0%9D%99%AE%F0%9D%99%96-%F0%9D%98%BD%F0%9D%99%8A%F0%9D%99%8F-02-08-3"
                    ),
                ],
                [
                    InlineKeyboardButton(
                       "جـروب الـدعـم..♡", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton(
                        "قـنـأة ألـسـوُرس..♡", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "اضـف الـبـوت لـ مـجـمـوعـتـك..♡",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
