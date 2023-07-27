import tkinter as tk
import tkinter.tix as tkx
from tkinter import messagebox as mb
from tkcalendar import DateEntry
from tkinter import ttk
import datetime
import sqlite3
import time

from Data.DB_Lockers import Locker, Tenant, History, create_lickers
from Display_views.display_lockers import rendering_lockers
from Display_views.information_table import mainInfoBlock

# Файл лого для окон
logo = 'Images/boxing.ico'

# Параметры основного окна
main_window = tk.Tk()
main_window.resizable(False, False)
main_window.title("Шкафчики")
main_window.iconbitmap(logo)
style = ttk.Style(main_window)
style.configure("vista")
main_window.state('zoomed')

# Переменные шаблонных png для отображения статуса
photo = tk.PhotoImage(file=r"States/no_key/locker.png")
photo_red = tk.PhotoImage(file=r"States/no_key/locker_red.png")
photo_green = tk.PhotoImage(file=r"States/no_key/locker_green.png")
photo_yellow = tk.PhotoImage(file=r"States/no_key/locker_yellow.png")
photo_key = tk.PhotoImage(file=r"States/key/locker_key.png")
photo_key_green = tk.PhotoImage(file=r"States/key/locker_key_green.png")
photo_key_red = tk.PhotoImage(file=r"States/key/locker_key_red.png")
photo_key_yellow = tk.PhotoImage(file=r"States/key/locker_key_yellow.png")

context = [photo, photo_red, photo_green, photo_yellow, photo_key, photo_key_green, photo_key_red, photo_key_yellow]

# ОТРИСОВКА ШКАФЧИКОВ
rendering_lockers(main_window, context)

# БЛОК ДОПОЛНИТЕЛЬНОЙ ИНФОРМАЦИИ
mainInfoBlock(main_window)

main_window.mainloop()
