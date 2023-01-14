from Data.DB_Lockers import Locker, Tenant, History, create_lickers
from tkinter import ttk
from tkinter import *
from Display_views.display_lockers import rendering_lockers

import tkinter as tk


"""БЛОК ДОПОЛНИТЕЛЬНОЙ ИНФОРМАЦИИ"""
#--------------------------------------------------------------------------------

def mainInfoBlock(parent):
	block_BOTTOM = Frame(parent)
	block_BOTTOM.pack(side=TOP, pady=10)

	def tabs(parent):
		# Родитель вкладок
		tab_control = ttk.Notebook(block_BOTTOM)  
		tab1 = ttk.Frame(tab_control) # 
		tab2 = ttk.Frame(tab_control) # 
		tab3 = ttk.Frame(tab_control) # 
		tab4 = ttk.Frame(tab_control) # 
		tab5 = ttk.Frame(tab_control) # 
		tab6 = ttk.Frame(tab_control) # 
		tab7 = ttk.Frame(tab_control) # 
		tab8 = ttk.Frame(tab_control) # 
		tab9 = ttk.Frame(tab_control) # 
		#ВАЖНО! Пакует все вкладки на странице
		tab_control.pack(expand=1, fill=BOTH, side=TOP)

		def update():
			tab_control.destroy()
			return(tabs(parent))

		#Вкладки
		#---------------------------------------------------------------
		
		tab1 = ttk.Frame(tab_control, width=1340, height=600)
		tab_control.add(tab1, text='Общая информация')

		lock_free = Locker.select().where(Locker.status == 'Пуст')
		free_lock = len(lock_free)

		free_lockers = Label(tab1, text=f'Свободны: {free_lock}', font="12")
		free_lockers.pack(anchor=W, pady="5")

		lock_busy = Locker.select().where(Locker.status == 'Просрочен')
		busy_lock = len(lock_busy)

		busy_lockers = Label(tab1, text=f'Просрочены: {busy_lock}', font="12")
		busy_lockers.pack(anchor=W, pady="5")

		lock_faulty = Locker.select().where(Locker.status == 'Поврежден')
		faulty_lock = len(lock_faulty)

		faulty_lockers = Label(tab1, text=f'Повреждены: {faulty_lock}', font="12")
		faulty_lockers.pack(anchor=W, pady="5")

		lock_noKey = Locker.select().where(Locker.spare_key == False)
		noKey_lock = len(lock_noKey)

		noKey_lockers = Label(tab1, text=f'Без запасного ключа: {noKey_lock}', font="12")
		noKey_lockers.pack(anchor=W, pady="5")


		Update_btn = Button(tab1, text='Обновить', font="12", command = update)
		Update_btn.pack(anchor=W, pady="5")
	
		#---------------------------------------------------------------

		tab2 = ttk.Frame(tab_control, width=1340, height=600)
		tab_control.add(tab2, text='Просрочены')

		prosrochen = Locker.select().where(Locker.status == 'Просрочен')

		if prosrochen:

			tree21 = ttk.Treeview(tab2, column=(
						"column1",
						"column2",
						"column3",
						"column4",
						"column5",
						"column6",  
								), 
						show='headings')
			tree21.heading("#1", text="№")
			tree21.column("#1", minwidth=0, width=50, stretch=NO, anchor=CENTER)
	
			tree21.heading("#2", text="Арендатор")
			tree21.column("#2", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree21.heading("#3", text="Телефон")
			tree21.column("#3", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree21.heading("#4", text="До")
			tree21.column("#4", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree21.heading("#5", text="Комментарий")
			tree21.column("#5", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree21.heading("#6", text="Оплачено")
			tree21.column("#6", minwidth=0, width=252, stretch=NO, anchor=CENTER)
			tree21.pack()
			
			
			for i in prosrochen:
				ten = Tenant.get(Tenant.locker_id == i.id)
				tree21.insert('', tk.END, values= (i.id, ten.name, ten.number, ten.end_date_of_the_lease, i.comment, i.rental_counter))
				tree21.pack()
				tree21.config(height=600)

		else:
			No_Pay = Label(tab2, text='Просточенных оплат нет')
			No_Pay.config(height=600, width=1340)
			No_Pay.pack()		

		#---------------------------------------------------------------

		tab3 = ttk.Frame(tab_control)
		tab_control.add(tab3, text='Список арендаторов')

		arendator = Locker.select()
		tenant = Tenant.select()

		if tenant:
		
			tree_arendator = ttk.Treeview(tab3, column=(
						"column1",
						"column2",
						"column3",
						"column4",
						"column5",
						"column6",  
								), 
						show='headings')
			tree_arendator.heading("#1", text="№")
			tree_arendator.column("#1", minwidth=0, width=50, stretch=NO, anchor=CENTER)
	
			tree_arendator.heading("#2", text="Арендатор")
			tree_arendator.column("#2", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_arendator.heading("#3", text="Телефон")
			tree_arendator.column("#3", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_arendator.heading("#4", text="До")
			tree_arendator.column("#4", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_arendator.heading("#5", text="Комментарий")
			tree_arendator.column("#5", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_arendator.heading("#6", text="Оплачено")
			tree_arendator.column("#6", minwidth=0, width=252, stretch=NO, anchor=CENTER)

			
			for i in arendator:
				tt = Tenant.select().where(Tenant.locker_id == i.id)
				for t in tt:
					tree_arendator.insert('', tk.END, values= (i.id, t.name, t.number, t.end_date_of_the_lease, i.comment, i.rental_counter))
					tree_arendator.pack()
					tree_arendator.config(height=600)

		else:
			No_Men = Label(tab3, text='Арендаторы отсутствуют')
			No_Men.config(height=600, width=1340)
			No_Men.pack()
		#---------------------------------------------------------------

		tab4 = ttk.Frame(tab_control)
		tab_control.add(tab4, text='Без запасного ключа')

		noKey = Locker.select().where(Locker.spare_key == False)

		if noKey:

			tree_noKey = ttk.Treeview(tab4, column=(
						"column1",
						"column2",
						"column3",
						"column4",
						"column5",
						"column6",  
								), 
						show='headings')
			tree_noKey.heading("#1", text="№")
			tree_noKey.column("#1", minwidth=0, width=50, stretch=NO, anchor=CENTER)
	
			tree_noKey.heading("#2", text="Арендатор")
			tree_noKey.column("#2", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_noKey.heading("#3", text="Телефон")
			tree_noKey.column("#3", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_noKey.heading("#4", text="До")
			tree_noKey.column("#4", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_noKey.heading("#5", text="Комментарий")
			tree_noKey.column("#5", minwidth=0, width=258, stretch=NO, anchor=CENTER)
	
			tree_noKey.heading("#6", text="Оплачено")
			tree_noKey.column("#6", minwidth=0, width=252, stretch=NO, anchor=CENTER)
			
			for i in noKey:
				tenant_locker = Tenant.select().where(Tenant.locker_id == i.id)
				t1, t2, t3 = "--------", "--------", "--------"
		
				for t in tenant_locker:
					t1, t2, t3 = t.name, t.number, t.end_date_of_the_lease	
					tree_noKey.insert('', tk.END, values= (i.id, t.name, t.number, t.end_date_of_the_lease, i.comment, i.rental_counter))
					tree_noKey.config(height=600)
					tree_noKey.pack()

		else:
			No_Key = Label(tab4, text='Все запасные ключи имеются в наличии')
			No_Key.config(height=600, width=1340)
			No_Key.pack()			

	tabs(block_BOTTOM)
