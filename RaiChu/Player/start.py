
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
        f"""[👋](https://telegra.ph/file/07774703ca98686f51fd4.jpg)
**مرحبا بك فـ سـوُرس سـافو يتيح لك تشغيل الموسيقي والفيديو بدون اي مشكله وبدون تهنيج 🤍😊
        
امـامـك الـبـوت الـخـاص بـنـا..♡ [𝘽𝙤𝙩 𝚂𝙰𝚅𝙾](https://t.me/B8stat_bot)
نـتـمنـي لـكـم الـاسـتـمـتـاع بـهـذا الـبـوت 😇**

💞  تم برمجة البوت بواسطة 

⋆  [Mostafa Ali](t.me/s_a_s_a_3li)
⋆  [Emperor Hassan](https://t.me/theemperorhb)
 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور البوت..♡", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "مـبرمج السـورس..♡", url="https://t.me/s_a_s_a_3li"
                    ),
                    InlineKeyboardButton(
                        "الـاوامـر..♡", url="https://t.me/DEV_SAVO/26"
                    ),
                ],
                [
                    InlineKeyboardButton(
                       "جـروب الـدعـم..♡", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton(
                        "قـنـأة السـورس..♡", url=f"https://t.me/{UPDATES_CHANNEL}"),
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
