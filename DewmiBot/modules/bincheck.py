import requests
from telethon import events
from DewmiBot import telethn as rose

@rose.on(events.NewMessage(pattern="^[!?/]bin"))
async def bincheck(event):
    xx = await event.reply("`Processing.....`")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
        res = url.json()
        vendor = res['data']['vendor']
        type = res['data']['type']
        level = res['data']['level']
        bank = res['data']['bank']
        country = res['data']['country']
        emoji = res['data']['countryInfo']['emoji']
        me = (await event.client.get_me()).username

        valid = f"""
<b>┏━━━━━━━━━━━━━━━━━━</b>
<b>┠⌬ BIN   :</b> <code>{input} {emoji}</code>
<b>┠⌬ BRAND :</b> <code>{vendor}</code>
<b>┠⌬ TYPE  :</b> <code>{type}</code>
<b>┠⌬ LEVEL :</b> <code>{level}</code>
<b>┠⌬ BANK  :</b> <code>{bank}</code>
<b>┠⌬ COUNTRY :</b> <code>{country}</code>
<b>┗━━━━━━━━━━━━━━━━━━</b>
"""
        await xx.edit(valid, parse_mode="HTML")
    except IndexError:
       await xx.edit("Plese provide a bin to check\n__`/bin yourbin`__")
    except KeyError:
        me = (await event.client.get_me()).username
        await xx.edit(f"**❌ INVALID BIN ❌**\n\n**Bin -** `{input}`\n**Status -** `Invalid Bin`\n\n**Checked By -** @{me}\n**User-ID - {event.sender_id}**")
