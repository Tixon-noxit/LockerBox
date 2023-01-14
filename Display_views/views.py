from Data.DB_Lockers import Locker, Tenant, History, create_lickers
from tkinter import messagebox as mb
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import *
from .status_locker import stat

import tkinter as tk
import datetime





# Файл для хранения логов операций

logs = 'Logs/The_event_log.txt'




"""БЛОК ИНФОРМАЦИИ О ВЫБРАННОМ ШКАФЧИКЕ"""
#--------------------------------------------------------------------------------
def locker(arg, arg2, context): # Имя, Название

	photo = context[0] 
	photo_red = context[1]
	photo_green = context[2]
	photo_yellow = context[3]
	photo_key = context[4]
	photo_key_green = context[5]
	photo_key_red = context[6]
	photo_key_yellow = context[7]
	logo = 'Images/boxing.ico'
	newWindow = Toplevel(arg)
	newWindow.geometry('500x300+380+200')
	newWindow.iconbitmap(logo)
	newWindow.title(arg2)
	newWindow.resizable(False, False)
	newWindow.focus_force()
	newWindow.grab_set()

	lock = Locker.get(Locker.name == arg2)
	now = datetime.datetime.today() # Дата в данный момент
	rental = 'foo'
	num = 'foo'
	date_rental = 'foo'
	st = f"Тестовый текст!"

	for tenant in lock.tenants: # Вывод информации об арендаторе
		rental =  tenant.name
		num = tenant.number
		date_rental = tenant.end_date_of_the_lease
		date_time_obj = datetime.datetime.strptime(date_rental, '%d/%m/%Y')
		tp = date_time_obj - now # Время до/после даты последнего продления/изменения
		tp2 = str(tp)
		time_pay = int(tp2.split()[0])

	if lock.status != 'Пуст' and lock.status != 'Поврежден':
		if time_pay <= 0:
			st = f"Просрочен на {abs(time_pay)} суток!"
		else:
			st = f"До конца аренды {time_pay} суток."
	else:
		st = '--------'
		rental = '--------'
		num = '--------'
		date_rental = '--------'

	label_name = Label(newWindow, text = "Именование:")
	label_name.place(x=100, y=37, anchor="e", height=20, width=95, bordermode=OUTSIDE)
	label_name = Label(newWindow, text = arg2)
	label_name.place(x=150, y=37, anchor="w", height=20, width=200, bordermode=OUTSIDE)

	labeljob = Label(newWindow, text = "Статус:")
	labeljob.place(x=100, y=67, anchor="e", height=20, width=95, bordermode=OUTSIDE)
	labeljob = Label(newWindow, text = lock.status)
	labeljob.place(x=150, y=67, anchor="w", height=20, width=200, bordermode=OUTSIDE)

	labelnum = Label(newWindow, text = "Арендатор:")
	labelnum.place(x=100, y=97, anchor="e", height=20, width=95, bordermode=OUTSIDE)
	labelnum = Label(newWindow, text = rental)
	labelnum.place(x=150, y=97, anchor="w", height=20, width=200, bordermode=OUTSIDE)

	labelnum1 = Label(newWindow, text = "Телефон:")
	labelnum1.place(x=100, y=127, anchor="e", height=20, width=95, bordermode=OUTSIDE)
	labelnum1 = Label(newWindow, text = num)
	labelnum1.place(x=150, y=127, anchor="w", height=20, width=200, bordermode=OUTSIDE)

	labelnum2 = Label(newWindow, text = "Срок аренды:")
	labelnum2.place(x=100, y=157, anchor="e", height=20, width=95, bordermode=OUTSIDE)
	labelnum2t = Label(newWindow, text = f'{lock.comment} | {st} |')
	labelnum2t.place(x=150, y=157, anchor="w", height=20, width=200, bordermode=OUTSIDE)

	labelnum3 = Label(newWindow, text = "Аренда до:")
	labelnum3.place(x=100, y=187, anchor="e", height=20, width=95, bordermode=OUTSIDE)
	labelnum3 = Label(newWindow, text = date_rental)
	labelnum3.place(x=150, y=187, anchor="w", height=20, width=200, bordermode=OUTSIDE)

	labelnum4 = Label(newWindow, text = "Оплачено:")
	labelnum4.place(x=100, y=217, anchor="e", height=20, width=95, bordermode=OUTSIDE)
	labelnum4 = Label(newWindow, text = lock.rental_counter)
	labelnum4.place(x=150, y=217, anchor="w", height=20, width=200, bordermode=OUTSIDE)


	# Изменение данных о шкафчике
	def change(arg, arg2): 
		newWindow.destroy()
		change_Window = Toplevel(arg)
		change_Window.geometry('500x300+380+200')
		change_Window.iconbitmap(logo)
		change_Window.title(f"Редактировать {arg2}")
		change_Window.resizable(False, False)
		change_Window.focus_force()
		change_Window.grab_set()

		lock = Locker.get(Locker.name == arg2)

		rental =  '--------'
		num = '--------'
		place_com = f"{now.day}/{now.month}/{now.year}"


		# Вывод информации об арендаторе
		for tenant in lock.tenants: 
			rental =  tenant.name
			num = tenant.number
			place_com = tenant.end_date_of_the_lease

		label_name = Label(change_Window, text = "Именование:")
		label_name.place(x=100, y=37, anchor="e", height=20, width=95, bordermode=OUTSIDE)
		label_name = Label(change_Window, text = arg2)
		label_name.place(x=150, y=37, anchor="w", height=20, width=200, bordermode=OUTSIDE)
	
		labelnum = Label(change_Window, text = "Статус:")
		labelnum.place(x=100, y=67, anchor="e", height=20, width=95, bordermode=OUTSIDE)


		status_list = ['Поврежден', 'Просрочен', 'Аренда. OK', 'Пуст']
		Operatorcombo_status = ttk.Combobox(change_Window)
		Operatorcombo_status['values'] = status_list
		place_n = lock.status
		Operatorcombo_status.insert('', place_n)
		Operatorcombo_status.current() 
		Operatorcombo_status.place(x=150, y=67, anchor="w", height=20, width=200, bordermode=OUTSIDE)
		
		labelpl = Label(change_Window, text = "Арендатор:")
		labelpl.place(x=100, y=97, anchor="e", height=20, width=95, bordermode=OUTSIDE)
		labelpl1 = Entry(change_Window)
		labelpl1.insert(0, rental)
		labelpl1.place(x=150, y=97, anchor="w", height=20, width=200, bordermode=OUTSIDE)
		
		labeladm = Label(change_Window, text = "Телефон:")
		labeladm.place(x=100, y=127, anchor="e", height=20, width=95, bordermode=OUTSIDE)
		labelpln = Entry(change_Window)
		labelpln.insert(0, num)
		labelpln.place(x=150, y=127, anchor="w", height=20, width=200, bordermode=OUTSIDE)

		labeladm = Label(change_Window, text = "Срок аренды:")
		labeladm.place(x=100, y=157, anchor="e", height=20, width=95, bordermode=OUTSIDE)
		status_list1 = ['Месяц', 'Полгода', 'Год']
		Operatorcombo_place1 = ttk.Combobox(change_Window)
		Operatorcombo_place1['values'] = status_list1
		place_n1 = lock.comment
		Operatorcombo_place1.insert('', place_n1)
		Operatorcombo_place1.current() 
		Operatorcombo_place1.place(x=150, y=157, anchor="w", height=20, width=200, bordermode=OUTSIDE)
	
		labelcom = Label(change_Window, text = "Аренда до:")
		labelcom.place(x=100, y=187, anchor="e", height=20, width=95, bordermode=OUTSIDE)

		calendar = DateEntry(change_Window,locale='ru_RU', date_pattern='dd/MM/yyyy', textvariable=place_com)
		calendar.delete(0, 'end')
		calendar.insert('', place_com)
		calendar.place(x=150, y=187, anchor="w", height=20, width=200, bordermode=OUTSIDE)

		labeladm = Label(change_Window, text = "Запасной ключ:")
		labeladm.place(x=100, y=217, anchor="e", height=20, width=95, bordermode=OUTSIDE)

		status_key = ['Присутствует', 'Отсутствует']
		Operatorcombo_key = ttk.Combobox(change_Window)
		Operatorcombo_key['values'] = status_key

		place_key = lock.spare_key
		if lock.spare_key == 1:
			place_key = "Присутствует"
		else:
			place_key = "Отсутствует"
		Operatorcombo_key.insert('', place_key)
		Operatorcombo_key.place(x=150, y=217, anchor="w", height=20, width=200, bordermode=OUTSIDE)

		labelasum = Label(change_Window, text = "Оплачено:")
		labelasum.place(x=100, y=247, anchor="e", height=20, width=95, bordermode=OUTSIDE)
		labelpsumentry = Entry(change_Window)
		labelpsumentry.insert(0, lock.rental_counter)
		labelpsumentry.place(x=150, y=247, anchor="w", height=20, width=200, bordermode=OUTSIDE)

		
	
		def save_visit():

			lock.status = Operatorcombo_status.get() # Статус

			key = Operatorcombo_key.get()
			if key == 'Присутствует':
				key = 1
			else:
				key = 0
			lock.spare_key = key # Запасной ключ

			lock.comment = Operatorcombo_place1.get() # Комментарий

			summ = labelpsumentry.get() # Оплачено
			lock.rental_counter = summ
			
			# Арендатор
			rental = labelpl1.get()
			num = labelpln.get()
			arenda = calendar.get()

			# save update
			if lock.tenants.count() == 0:
				Tenant.create(name=rental, locker_id = lock.id, number = num, end_date_of_the_lease = arenda)
				History.create(comment = lock.status, locker = lock.id, tenant = rental, number = num, summ = summ, end_date_of_the_lease = arenda, key = key, srock = lock.comment)
				f = open(logs, 'a')
				f.write(f"Дата: {now}. К {lock.name} добавлен арендатор {rental} / номер {num} на срок {lock.comment} до {arenda}. Оплачено {summ}. Запасной ключ {place_key}\n")
				f.close()
			else:	
				tenant.name = rental
				tenant.locker_id = lock.id
				tenant.number = num
				tenant.end_date_of_the_lease = arenda
				tenant.save()
				History.create(comment = lock.status, locker = lock.id, tenant = rental, number = num, summ = summ, end_date_of_the_lease = arenda, key = place_key, srock = lock.comment)
				f = open(logs, 'a')
				f.write(f"Дата: {now}. У {lock.name} изменен арендатор {rental} / номер {num} на срок {lock.comment} до {arenda}. Оплачено {summ}. Запасной ключ {place_key}\n")
				f.close()	
			lock.save()
			stat(arg, arg2, context)

			try:
				mb.showinfo("Успех!", "Изменения успешно внесены!")
				change_Window.destroy()
			except:
				mb.showerror("Ошибка!", "Ошибка при внесении изменений!")




		btn_save = Button(change_Window, text="Сохранить", 
			width=10, height=1, anchor="n", command = save_visit)
		btn_save.place(relx=0.95, y=280, anchor="e")



	# Хотите освободить шкафчик?
	def delete_locker(): 
		answer = mb.askyesno(
			title="Вопрос", 
			message=f"Освободить {arg2}?")

		if answer:
			lock.status = 'Пуст'
			lock.save()
			key = 'foo'
			mb.showinfo("Успех!", "Шкафчик освобожден!")

			# Удаление закрепленного арендатора
			for tenant in lock.tenants: 
				tenant.delete_instance()
				if lock.spare_key == 1:
					key = 'Присутствует' 
					arg.config(image=photo_key)
				else:
					key = 'Отсутствует'
					arg.config(image=photo)
				f = open(logs, 'a')
				f.write(f"Дата: {now}. {lock.name} освобожден! Запасной ключ {key}\n")
				f.close()
				History.create(comment = lock.status, locker = lock.id, tenant = '--------', number = '--------', summ = '--------', end_date_of_the_lease = '--------', key = lock.spare_key, srock = '--------')
				stat(arg, arg2, context)
				change_Window.destroy()			
		else:
			mb.showerror("Ошибка!", "Ошибка освобождения шкафчика!")



	def history(arg, arg2):
		newWindow.destroy()
		history_Window = Toplevel(arg)
		history_Window.geometry('880x300+280+200')
		history_Window.title(f"История {arg2}")
		history_Window.iconbitmap(logo)
		history_Window.resizable(False, False)
		history_Window.focus_force()
		history_Window.grab_set()

		lock = Locker.get(Locker.name == arg2)

		tree_history = ttk.Treeview(history_Window, column=(
					"column1", 
					"column2", 
					"column3",
					"column4",
					"column5",
					"column6", 
					),
					show='headings')
		tree_history.heading("#1", text="Дата")
		tree_history.column("#1",minwidth=0,width=68, stretch=NO, anchor=CENTER)
		tree_history.heading("#2", text="Арендатор")
		tree_history.column("#2",minwidth=0,width=200, stretch=NO, anchor=CENTER)
		tree_history.heading("#3", text="Телефон")
		tree_history.column("#3",minwidth=0,width=130, stretch=NO, anchor=CENTER)
		tree_history.heading("#4", text="Зап.ключ")
		tree_history.column("#4",minwidth=0,width=130, stretch=NO, anchor=CENTER)
		tree_history.heading("#5", text="Срок аренды")
		tree_history.column("#5",minwidth=0,width=213, stretch=NO, anchor=CENTER)
		tree_history.heading("#6", text="Оплачено")
		tree_history.column("#6",minwidth=0,width=130, stretch=NO, anchor=CENTER)
		tree_history.pack(expand=1, anchor=NW, fill="both")

		record = History.select().where(History.locker_id == lock.id)	
		for recording in record:
			if recording.key == 1:
				recording.key = "Присутствует"
			else:
				recording.key = "Отсутствует"	
			tree_history.insert('', tk.END, values=[recording.created_at, recording.tenant_id, recording.number,
													recording.key, recording.srock, recording.summ])
		
		
		# Скролбар история
		scroll = Scrollbar(tree_history)
		scroll.pack(side = 'right', fill = 'y')
		scroll['command'] =tree_history.yview
		tree_history['yscrollcommand'] = scroll.set	
							

	# Кнопки окна истории шкафчика
	btn_history = Button(newWindow, text="История", 
			        	width=10, height=1, anchor="n", command = lambda: history(arg,arg2))
	btn_history.place(relx=0.60, y=280, anchor="e")

	btn_change = Button(newWindow, text="Изменить", 
			        	width=10, height=1, anchor="n", command = lambda: change(arg,arg2))
	btn_change.place(relx=0.78, y=280, anchor="e")

	btn_change = Button(newWindow, text="Освободить", 
			        	width=10, height=1, anchor="n", command = delete_locker)
	btn_change.place(relx=0.96, y=280, anchor="e")
