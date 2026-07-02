from data_base import Hider
from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel
from tkinter import *
from tkinter import messagebox as msg
import os
from pyautogui import size, moveTo
import pyautogui as ui
from tkinter import simpledialog
import keyboard as key
from time import sleep
import threading as td

ui.FAILSAFE = False
w = Tk()
w.withdraw()

while True:

    code = simpledialog.askstring("password", "پسورد را وارد کنید")

    if code == "MRT_data":

        break

    else:

        msg.showwarning("wrong password", "پسورد غلط است")

        continue
        

w.destroy()


class hider_view:

    def __init__(self):

        self.title = "hider ui"

        self.frames_list = []

        self.window = Tk()

        self.window_width = int(int(size().width) * (4 / 5))

        self.window_height = int(int(size().height) * (4 / 5))

        self.window.geometry(f"{self.window_width}x{self.window_height}")

        self.window.resizable(width=False, height=False)

        self.frame_width = self.window_width * (4 / 5)

        self.frame_height = self.window_height * (4.5 / 5)

        self.data_base = Hider()

        key.add_hotkey("e+x", lambda: self.quit_exigent_mode())

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #:::::::::::::::::: MAIN PAGE :::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        self.main_Frame = CTkFrame(
            self.window,
            width=self.frame_width,
            height=self.frame_height,
            fg_color="#90EE90",
            corner_radius=40,
        )

        self.main_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

        self.frames_list.append(self.main_Frame)

        CTkLabel(
            self.main_Frame,
            text="Hider",
            fg_color="#90EE90",
            bg_color="#90EE90",
            font=("B Nazanin", 35, "bold"),
        ).place(x=self.frame_width * 2 / 5, y=self.frame_height * 0.25 / 10)

        self.hide_button = CTkButton(
            self.main_Frame,
            text="hide",
            bg_color="#90EE90",
            fg_color="red",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 1.35 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="#FCA5A5",
            command=self.goto_hide,
        )

        self.hide_button.place(
            x=self.frame_width * 1.1 / 5, y=self.frame_height * 1.5 / 8
        )

        self.group_hide_button = CTkButton(
            self.main_Frame,
            text="group hide",
            bg_color="#90EE90",
            fg_color="red",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 1 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="#FCA5A5",
            command=self.goto_group_hide,
        )

        self.group_hide_button.place(
            x=self.frame_width * 2.5 / 5, y=self.frame_height * 1.5 / 8
        )

        self.load_button = CTkButton(
            self.main_Frame,
            text="load",
            bg_color="#90EE90",
            fg_color="green",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 1.35 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="lightgreen",
            command=self.goto_load,
        )

        self.load_button.place(
            x=self.frame_width * 1.1 / 5, y=self.frame_height * 3 / 8
        )

        self.random_load_button = CTkButton(
            self.main_Frame,
            text="random load",
            bg_color="#90EE90",
            fg_color="green",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 0.6 / 5,
            height=self.frame_height * 0.9 / 10,
            font=("B Nazanin", 22, "bold"),
            text_color="black",
            hover_color="lightgreen",
            command=self.goto_random_load,
        )

        self.random_load_button.place(
            x=self.frame_width * 2.5 / 5, y=self.frame_height * 3 / 8
        )

        self.show_button = CTkButton(
            self.main_Frame,
            text="my files",
            bg_color="#90EE90",
            fg_color="green",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="lightgreen",
            command=self.show,
        )

        self.show_button.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 4.5 / 8
        )

        self.exit_button = CTkButton(
            self.main_Frame,
            text="exit",
            bg_color="#90EE90",
            fg_color="red",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="#FCA5A5",
            command=self.exit,
        )

        self.exit_button.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 6 / 8
        )

        self.exigent_mode_button = CTkButton(
            self.main_Frame,
            text="exigent mode",
            bg_color="#90EE90",
            fg_color="black",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="white",
            hover_color="gray",
            command=self.run_exigent_mode,
        )

        self.exigent_mode_button.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 7 / 8
        )

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #:::::::::::::::::: HIDE PAGE :::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        self.hide_Frame = CTkFrame(
            self.window,
            width=self.frame_width,
            height=self.frame_height,
            fg_color="#90EE90",
            corner_radius=40,
        )

        self.hide_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

        self.hide_Frame.place_forget()

        self.frames_list.append(self.hide_Frame)

        CTkLabel(
            self.hide_Frame,
            text="Hide",
            fg_color="#90EE90",
            bg_color="#90EE90",
            font=("B Nazanin", 35, "bold"),
        ).place(x=self.frame_width * 2 / 5, y=self.frame_height * 0.25 / 10)

        self.file_path_hide_entry = CTkEntry(
            self.hide_Frame,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            border_width=3,
            corner_radius=10,
            placeholder_text="آدرس فایل هدف",
            border_color="black",
        )

        self.file_path_hide_entry.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 1.5 / 8
        )

        self.file_name_hide_entry = CTkEntry(
            self.hide_Frame,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            border_width=3,
            corner_radius=10,
            placeholder_text="نام فایل در پایگاه داده",
            border_color="black",
        )

        self.file_name_hide_entry.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 3 / 8
        )

        CTkButton(
            self.hide_Frame,
            text="hide",
            bg_color="#90EE90",
            fg_color="blue",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="lightblue",
            command=self.hide,
        ).place(x=self.frame_width * 1.4 / 5, y=self.frame_height * 4.5 / 8)

        CTkButton(
            self.hide_Frame,
            text="back",
            bg_color="#90EE90",
            fg_color="red",
            border_width=3,
            corner_radius=50,
            width=self.frame_width * 0.5 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="#FCA5A5",
            command=self.back,
        ).place(x=0, y=0)

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #:::::::::::::::::: GROUP HIDE PAGE :::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        self.group_hide_Frame = CTkFrame(
            self.window,
            width=self.frame_width,
            height=self.frame_height,
            fg_color="#90EE90",
            corner_radius=40,
        )

        self.group_hide_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

        self.group_hide_Frame.place_forget()

        self.frames_list.append(self.group_hide_Frame)

        CTkLabel(
            self.group_hide_Frame,
            text="Group Hide",
            fg_color="#90EE90",
            bg_color="#90EE90",
            font=("B Nazanin", 35, "bold"),
        ).place(x=self.frame_width * 1.5 / 5, y=self.frame_height * 0.25 / 10)

        self.folder_path_hide_entry = CTkEntry(
            self.group_hide_Frame,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            border_width=3,
            corner_radius=10,
            placeholder_text="آدرس پوشه هدف",
            border_color="black",
        )

        self.folder_path_hide_entry.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 1.5 / 8
        )

        CTkButton(
            self.group_hide_Frame,
            text="group hide",
            bg_color="#90EE90",
            fg_color="blue",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="lightblue",
            command=self.group_hide,
        ).place(x=self.frame_width * 1.4 / 5, y=self.frame_height * 2.5 / 8)

        CTkButton(
            self.group_hide_Frame,
            text="back",
            bg_color="#90EE90",
            fg_color="red",
            border_width=3,
            corner_radius=50,
            width=self.frame_width * 0.5 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="#FCA5A5",
            command=self.back,
        ).place(x=0, y=0)

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #:::::::::::::::::: LOAD PAGE :::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        self.load_Frame = CTkFrame(
            self.window,
            width=self.frame_width,
            height=self.frame_height,
            fg_color="#90EE90",
            corner_radius=40,
        )

        self.load_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

        self.load_Frame.place_forget()

        self.frames_list.append(self.load_Frame)

        CTkLabel(
            self.load_Frame,
            text="load",
            fg_color="#90EE90",
            bg_color="#90EE90",
            font=("B Nazanin", 35, "bold"),
        ).place(x=self.frame_width * 2 / 5, y=self.frame_height * 0.25 / 10)

        CTkButton(
            self.load_Frame,
            text="back",
            bg_color="#90EE90",
            fg_color="red",
            border_width=3,
            corner_radius=50,
            width=self.frame_width * 0.5 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="#FCA5A5",
            command=self.back,
        ).place(x=0, y=0)

        self.file_name_load_entry = CTkEntry(
            self.load_Frame,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            border_width=3,
            corner_radius=10,
            placeholder_text="نام فایل در پایگاه داده",
            border_color="black",
        )

        self.file_name_load_entry.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 1.5 / 8
        )

        self.file_format_load_entry = CTkEntry(
            self.load_Frame,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            border_width=3,
            corner_radius=10,
            placeholder_text="فرمت فایل خروجی",
            border_color="black",
        )

        self.file_format_load_entry.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 3 / 8
        )

        CTkButton(
            self.load_Frame,
            text="load",
            bg_color="#90EE90",
            fg_color="blue",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="lightblue",
            command=self.load,
        ).place(x=self.frame_width * 1.4 / 5, y=self.frame_height * 4.5 / 8)

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #:::::::::::::::::: RANDOM LOAD PAGE ::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        self.random_load_Frame = CTkFrame(
            self.window,
            width=self.frame_width,
            height=self.frame_height,
            fg_color="#90EE90",
            corner_radius=40,
        )

        self.random_load_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

        self.random_load_Frame.place_forget()

        self.frames_list.append(self.random_load_Frame)

        CTkLabel(
            self.random_load_Frame,
            text="random load",
            fg_color="#90EE90",
            bg_color="#90EE90",
            font=("B Nazanin", 35, "bold"),
        ).place(x=self.frame_width * 1.5 / 5, y=self.frame_height * 0.25 / 10)

        CTkButton(
            self.random_load_Frame,
            text="back",
            bg_color="#90EE90",
            fg_color="red",
            border_width=3,
            corner_radius=50,
            width=self.frame_width * 0.5 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="#FCA5A5",
            command=self.back,
        ).place(x=0, y=0)

        self.name_feature_load_entry = CTkEntry(
            self.random_load_Frame,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            border_width=3,
            corner_radius=10,
            placeholder_text="کلمه مشترک بین گزینه ها",
            border_color="black",
        )

        self.name_feature_load_entry.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 1.5 / 8
        )

        self.item_load_entry = CTkEntry(
            self.random_load_Frame,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            border_width=3,
            corner_radius=10,
            placeholder_text="تعداد خروجی",
            border_color="black",
        )

        self.item_load_entry.place(
            x=self.frame_width * 1.4 / 5, y=self.frame_height * 3 / 8
        )

        CTkButton(
            self.random_load_Frame,
            text="random load",
            bg_color="#90EE90",
            fg_color="blue",
            border_width=3,
            corner_radius=10,
            width=self.frame_width * 2 / 5,
            font=("B Nazanin", 25, "bold"),
            text_color="black",
            hover_color="lightblue",
            command=self.random_load,
        ).place(x=self.frame_width * 1.4 / 5, y=self.frame_height * 4.5 / 8)

        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #:::::::::::::::::: EXIGENT PAGE ::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        self.exigent_Frame = CTkFrame(
            self.window,
            width=int(size().width),
            height=int(size().height),
            fg_color="black",
            corner_radius=40,
        )

        self.exigent_Frame.place(x=-1000, y=-1000)

        self.exigent_Frame.place_forget()

        self.frames_list.append(self.exigent_Frame)

        self.window.mainloop()

    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #:::::::::: GOTO FUNCTIONS:::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::

    def goto_hide(self):

        for i in self.frames_list:

            i.place_forget()

        self.hide_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

    def goto_group_hide(self):

        for i in self.frames_list:

            i.place_forget()

        self.group_hide_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

    def goto_load(self):

        for i in self.frames_list:

            i.place_forget()

        self.load_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

    def goto_random_load(self):

        for i in self.frames_list:

            i.place_forget()

        self.random_load_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

    def goto_exigent(self):

        for i in self.frames_list:

            i.place_forget()

        self.exigent_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

    def back(self):

        for i in self.frames_list:

            i.place_forget()

        self.main_Frame.place(
            x=self.window_width * (1 / 10), y=self.window_height * (0.5 / 10)
        )

    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #:::::::::: HIDE FUNCTIONS:::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::

    def hide(self):

        nones = ["", None]

        file_path = str(self.file_path_hide_entry.get())

        file_name = str(self.file_name_hide_entry.get())

        if file_path in nones or file_name in nones:

            msg.showwarning("blank field", "لطفا همه فیلد ها را پر کنید")

            return 0

        self.data_base.hide(file_path=file_path, save_name=file_name)

        self.file_path_hide_entry.delete(0, END)

        self.file_name_hide_entry.delete(0, END)

        msg.showinfo("hided", "your data Hided")

    def group_hide(self):

        folder_path = str(self.folder_path_hide_entry.get())

        try:

            result = self.data_base.group_hide(folder_path)

        except:

            msg.showerror("error", "folder not found")

        self.folder_path_hide_entry.delete(0, END)

        msg.showinfo("reslult", result)

    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #:::::::::: LOAD FUNCTIONS:::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::

    def load(self):

        file_name = str(self.file_name_load_entry.get())

        file_format = str(self.file_format_load_entry.get())

        self.data_base.load(file_name, file_format)

        self.file_name_load_entry.delete(0, END)

        self.file_format_load_entry.delete(0, END)

        msg.showinfo("loaded", "your data loaded")

    def random_load(self):

        nones = ["", None]

        name_feature = str(self.name_feature_load_entry.get())

        try:

            items = int(str(self.item_load_entry.get()))

        except:

            msg.showerror("invalid number", "لطفا یک عدد درست وارد کنید")

            return 0

        if name_feature in nones or items in nones:

            msg.showerror("blank field", "لطفا همه فیلد ها را به درستی پر کنید")

            return 0

        self.data_base.random_load(items, name_feature)

        self.name_feature_load_entry.delete(0, END)

        self.item_load_entry.delete(0, END)

        msg.showinfo("loaded", f"{items} data loaded randomly")

    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #:::::::::: SHOW FUNCTIONS:::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::

    def show(self):

        data = self.data_base.get_list()

        msg.showinfo("Item counts", f"you hade {len(data)} items up to now")

    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #:::::::::: EXIT FUNCTIONS:::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::

    def exit(self):

        check = msg.askyesno("exit?", "آیا خارج می شوید")

        if check == True:

            os._exit(1)

    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #:::::::::: EXIGENT FUNCTIONS::::::::::
    #::::::::::::::::::::::::::::::::::::::
    #::::::::::::::::::::::::::::::::::::::

    def mouse_lock(self):

        while True:

            moveTo(0, 0)

            if key.is_pressed("e+x"):

                break

    def run_exigent_mode(self):

        self.window.geometry(f"{size().width}x{size().height}")
        self.window.geometry("+0+0")
        self.window.config(bg="black")
        self.goto_exigent()
        a = td.Thread(target=self.mouse_lock)

        a.start()

        a.setDaemon(True)

    def quit_exigent_mode(self):

        self.window.geometry(f"{self.window_width}x{self.window_height}")

        self.window.config(bg="white")

        self.back()


MRT = hider_view()
