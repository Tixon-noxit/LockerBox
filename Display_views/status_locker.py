from Data.DB_Lockers import Locker, Tenant, History, create_lickers
from tkinter import *

import datetime


"""БЛОК СТАТУСА"""
# Вывод и обновление статуса шкафчиков
def stat(arg, arg2, context): # arg-переменная-имя arg2-Название шкафчика

	lock = Locker.get(Locker.name == arg2)
	now = datetime.datetime.now() # Дата в данный момент
	if lock.status == 'Поврежден': # Выявление поврежденных шкафчиков
		if lock.spare_key == 1 and lock.status == 'Поврежден': # Проблемный с ключом
			arg.config(image=context[7])
		elif lock.spare_key == 0 and lock.status == 'Поврежден': # Проблемный без ключа
			arg.config(image=context[3])
	else:
		if lock.tenants.count() == 0: # Если за шкафчиком не закреплен арендатор
			lock.status = 'Пуст'
			lock.save()
			#print(f"{arg2} пуст!")
			if lock.spare_key == 1: # Пустой с ключом
				arg.config(image=context[4])
			elif lock.spare_key == 0: # Пустой без ключа
				arg.config(image=context[0])
		else:
			for tenant in lock.tenants:
				date_rental = tenant.end_date_of_the_lease
				date_time_obj = datetime.datetime.strptime(date_rental, '%d/%m/%Y')
				tp = date_time_obj - now # Время до/после даты последнего продления/изменения
				tp2 = str(tp)
				tp3 = tp2.partition('.')[0][0]
				try:
					time_pay = int(tp2.split()[0]) #(tp2.split()[0])
				except:
					time_pay = 0

				
		
			if time_pay == 0:
				#print(f"{arg2} сегодня последний день!")
				if lock.spare_key == 1: # Просрочен с ключом
					arg.config(image=context[6])
				else: 
					lock.spare_key == 0 # Просрочен без ключа
					arg.config(image=context[1])
			elif time_pay < 0:
				#print(f"{arg2} просрочен на {abs(time_pay)} дней!")
				if lock.spare_key == 1: # Просрочен с ключом
					arg.config(image=context[6])
				else: 
					lock.spare_key == 0 # Просрочен без ключа
					arg.config(image=context[1])
			else:
				#print(f"{arg2} до конца аренды {time_pay} дней.")
				if lock.spare_key == 1: # Ок с ключом
					arg.config(image=context[5])
				elif lock.spare_key == 0: # Ок без ключа
					arg.config(image=context[2])
