from telegram import Bot
from .models import MNSetup
from website.models import DeviceName
import asyncio
import asyncio, logging

logger = logging.getLogger('django')

TELEGRAM_BOT_TOKEN = '7595471571:AAFHCj8q_sUfIgFvby4WO20bsZGH3gCEj0c'
CHAT_ID = '-4528688279'

#Define bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def run_bot(messages, chat_id):
    text = '\n'.join(messages)
    await send_message(text, chat_id)


def check_alert(id,Temp,Humi,Volt):
    
    mnsetup = MNSetup.objects.get(id=id)
    device = DeviceName.objects.get(id=id)

    #logger.info(mnsetup.TempAlert)

    #Volt status 0=AlertDisable, 1=AlertEnable, 2 = Alerted, 3=WaitAcknowledge, 4=Acknowledge
    if mnsetup.VoltStatus != 0 :
        if mnsetup.VoltStatus == 3 :
            asyncio.run(send_message(device.DeviceName + ": Power Acknowledge!",CHAT_ID))
            mnsetup.VoltStatus = 4 #Acknowledge
            mnsetup.save()
        elif Volt < mnsetup.VoltAlert and mnsetup.VoltStatus in [1,2] :
            asyncio.run(send_message(device.DeviceName + ": Power Down!",CHAT_ID))
            mnsetup.VoltStatus = 2 #Alerted
            mnsetup.save()
        elif Volt > mnsetup.VoltAlert and mnsetup.VoltStatus != 1 :
            asyncio.run(send_message(device.DeviceName + ": Power Up!",CHAT_ID))
            mnsetup.VoltStatus = 1
            mnsetup.save()

    #Temperature status 0=AlertDisable, 1=AlertEnable, 2 = Alerted, 3=WaitAcknowledge, 4=Acknowledge
    if mnsetup.TempStatus != 0 :
        if mnsetup.TempStatus == 3 :
            asyncio.run(send_message(device.DeviceName + ": Temperature Acknowledge!",CHAT_ID))
            mnsetup.TempStatus = 4 #Acknowledge
            mnsetup.save()
        if Temp >= mnsetup.TempAlert and mnsetup.TempStatus in [1,2] :
            asyncio.run(send_message(device.DeviceName + ": "+ str(Temp) + "°C Temperature to high",CHAT_ID))
            mnsetup.TempStatus = 2 #Alerted
            mnsetup.save()
        elif Temp < mnsetup.TempAlert and mnsetup.TempStatus != 1 :
            asyncio.run(send_message(device.DeviceName + ": "+ str(Temp) + "°C Temperature back to normal!",CHAT_ID))
            mnsetup.TempStatus = 1
            mnsetup.save()

    #Humidity status 0=AlertDisable, 1=AlertEnable, 2 = Alerted, 3=WaitAcknowledge, 4=Acknowledge
    if mnsetup.HumiStatus != 0 :
        if mnsetup.HumiStatus == 3 :
            asyncio.run(send_message(device.DeviceName + ": Humidity Acknowledge!",CHAT_ID))
            mnsetup.HumiStatus = 4 #Acknowledge
            mnsetup.save()
        if Humi >= mnsetup.HumiAlert and mnsetup.HumiStatus in [1,2]:
            asyncio.run(send_message(device.DeviceName + ": "+ str(Humi) + "% Humidity to high",CHAT_ID))
            mnsetup.HumiStatus = 2 #Alerted
            mnsetup.save()
        elif Humi < mnsetup.HumiAlert and mnsetup.HumiStatus != 1 :
            asyncio.run(send_message(device.DeviceName + ": "+ str(Humi) + "% Humidity back to normal!",CHAT_ID))
            mnsetup.HumiStatus = 1
            mnsetup.save()

