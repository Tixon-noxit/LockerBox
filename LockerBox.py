from Data.DB_Lockers import Locker, Tenant, History, create_lickers
from tkinter import messagebox as mb
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import *
from Display_views.display_lockers import rendering_lockers
from Display_views.information_table import mainInfoBlock

import tkinter.tix as tkx
import tkinter as tk
import datetime
import sqlite3
import time


# Файл лого для окон
logo = 'Images/boxing.ico'

# Параметры основного окна 
root = Tk()
root.resizable(False, False)
root.title("Шкафчики")
root.iconbitmap(logo)
style = ttk.Style(root)
style.configure("vista")
root.state('zoomed')
 

# Переменные шаблонных png для отображения статуса
photo = PhotoImage(file = r"States/no_key/locker.png")
photo_red = PhotoImage(file = r"States/no_key/locker_red.png")
photo_green = PhotoImage(file = r"States/no_key/locker_green.png")
photo_yellow = PhotoImage(file = r"States/no_key/locker_yellow.png")
photo_key = PhotoImage(file = r"States/key/locker_key.png") 
photo_key_green = PhotoImage(file = r"States/key/locker_key_green.png")
photo_key_red = PhotoImage(file = r"States/key/locker_key_red.png")
photo_key_yellow = PhotoImage(file = r"States/key/locker_key_yellow.png")
#--------------------------------------------------------------------------------
context = [photo, photo_red, photo_green, photo_yellow, photo_key, photo_key_green, photo_key_red, photo_key_yellow]
	
""" ОТРИСОВКА ШКАФЧИКОВ """

rendering_lockers(root, context)


"""БЛОК ДОПОЛНИТЕЛЬНОЙ ИНФОРМАЦИИ"""
mainInfoBlock(root)

root.mainloop()
