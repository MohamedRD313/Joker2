import re

from telethon import Button, events
from telethon.events import CallbackQuery

from l313l.razan.resources.assistant import *
from l313l.razan.resources.mybot import *
from JoKeRUB import l313l
from ..core import check_owner
from ..Config import Config

JEP_IC = "https://telegra.ph/file/806e83ebc8c15da72c80d.jpg"
ROE = "**🦂 هـذه هي قائمة اوامـر سـورس العقرب**"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("اوامري") and event.query.user_id == bot.uid:
            buttons = [
                [Button.inline("🦂 اوامر الادمن 🦂", data="l313l0")],
                [
                    Button.inline("🦂 اوامر البوت 🦂", data="rozbot"),
                    Button.inline("🦂 الحساب 🦂", data="Jmrz"),
                    Button.inline("🦂 المجموعات 🦂", data="gro"),
                ],
                [
                    Button.inline("🦂 الصيغ و الجهات 🦂", data="sejrz"),
                    Button.inline("🦂 الحماية و تلكراف 🦂", data="grrz"),
                ],
                [
                    Button.inline("🦂 اوامر التسلية 🦂", data="tslrzj"),
                    Button.inline("🦂 الترحيبات والردود 🦂", data="r7brz"),
                ],
                [
                    Button.inline("🦂 اومر المساعدة 🦂", data="krrznd"),
                    Button.inline("🦂 الملصقات وصور 🦂", data="jrzst"),
                ],
                [
                    Button.inline("🦂 التكرار والتنظيف 🦂", data="krrznd"),
                    Button.inline("🦂 الترفيه 🦂", data="rfhrz"),
                ],
                [
                    Button.inline("🦂 التكرار والتنظيف 🦂", data="iiers"),
                    Button.inline("🦂 الملصقات وصور 🦂", data="jrzst"),
                ],
                [
                    Button.inline("🦂 الأكستـرا 🦂", data="iiers"),
                    Button.inline("🦂 الانتحال والتقليد 🦂", data="uscuxrz"),
                ],
            ]
            if JEP_IC and JEP_IC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    JEP_IC, text=ROE, buttons=buttons, link_preview=False
                )
            elif JEP_IC:
                result = builder.document(
                    JEP_IC,
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="JoKeRUB",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="اوامري"))
async def repo(event):
    if event.fwd_from:
        return
    lMl10l = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(lMl10l, "اوامري")
    await response[0].click(event.chat_id)
    await event.delete()


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"l313l0")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("الي بعدو", data="jrzst"),
      Button.inline("القائمة الرئيسية", data="ROE"),]]
    await event.edit(ROZADM, buttons=buttons)

@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"jrzst")))
@check_owner
async def _(event):
    butze = [
    [
     Button.inline("الي بعدو", data="tslrzj"),
     Button.inline("ارجع", data="l313l0")]]
    await event.edit(GRTSTI, buttons=butze)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"tslrzj")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="krrznd"),
     Button.inline("ارجع", data="jrzst")]]
    await event.edit(JMAN, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"krrznd")))
@check_owner
async def _(event):
    buttons = [
    [
      Button.inline("الي بعدو", data="rozbot"),
      Button.inline("ارجع", data="tslrzj")]]
    await event.edit(TKPRZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rozbot")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="Jmrz"),
     Button.inline("ارجع", data="krrznd")]]
    await event.edit(ROZBOT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"Jmrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="r7brz"),
     Button.inline("ارجع", data="rozbot")]]
    await event.edit(JROZT, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"r7brz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="sejrz"),
     Button.inline("ارجع", data="Jmrz")]]
    await event.edit(JMTRD, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"sejrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="gro"),
     Button.inline("ارجع", data="r7brz")]]
    await event.edit(ROZSEG, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"gro")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="grrz"),
     Button.inline("ارجع", data="sejrz")]]
    await event.edit(JMGR1,buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"grrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="iiers"),
     Button.inline("ارجع", data="gro")]]
    await event.edit(ROZPRV, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"iiers")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="rfhrz"),
     Button.inline("ارجع", data="grrz")]]
    await event.edit(HERP, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"rfhrz")))
@check_owner
async def _(event):
    buttons = [
    [
     Button.inline("الي بعدو", data="uscuxrz"),
     Button.inline("ارجع", data="iiers")]]
    await event.edit(T7SHIZ, buttons=buttons)


@l313l.tgbot.on(CallbackQuery(data=re.compile(rb"uscuxrz")))
@check_owner
async def _(event):
    buttons = [[Button.inline("ارجع  data="l313l0"),]]
    await event.edit(CLORN, buttons=buttons)
