from .status_locker import stat
from .views import locker
from tkinter import *






"""БЛОК ОТРИСОВКИ ШКАФЧИКОВ"""
#--------------------------------------------------------------------------------
def rendering_lockers(parent, context):

	# stat(arg, arg2, context)

	block_TOP = Frame(parent)
	block_TOP.pack(expand=1, side=TOP)

	# Блоки шкафчиков
	lockers_1 = Frame(block_TOP, padx="10")
	lockers_1.pack(side=LEFT)
	row_1 = Frame(lockers_1)
	row_1.pack()
	row_2 = Frame(lockers_1)
	row_2.pack()
	row_3 = Frame(lockers_1)
	row_3.pack()
	row_4 = Frame(lockers_1)
	row_4.pack()

	photo = context[0]

	btn = Button(row_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn, 'Шкафчик №1', context))
	btn.pack(side=LEFT) 
	
	btn2 = Button(row_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn2, 'Шкафчик №2', context))
	btn2.pack(side=LEFT)
	
	btn3 = Button(row_1, text="Click Me", background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn3, 'Шкафчик №3', context))
	btn3.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn4 = Button(row_2, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn4, 'Шкафчик №4', context))
	btn4.pack(side=LEFT)
	
	btn5 = Button(row_2, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn5, 'Шкафчик №5', context))
	btn5.pack(side=LEFT)
	
	btn6 = Button(row_2, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn6, 'Шкафчик №6', context))
	btn6.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn7 = Button(row_3, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn7, 'Шкафчик №7', context))
	btn7.pack(side=LEFT)
	
	btn8 = Button(row_3, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn8, 'Шкафчик №8', context))
	btn8.pack(side=LEFT)
	
	btn9 = Button(row_3, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn9, 'Шкафчик №9', context))
	btn9.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn10 = Button(row_4, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn10, 'Шкафчик №10', context))
	btn10.pack(side=LEFT)
	
	btn11 = Button(row_4, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn11, 'Шкафчик №11', context))
	btn11.pack(side=LEFT)
	
	btn12 = Button(row_4, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn12, 'Шкафчик №12', context))
	btn12.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	
	lockers_2 = Frame(block_TOP, padx="5")
	lockers_2.pack(side=LEFT)
	
	row_1_1 = Frame(lockers_2)
	row_1_1.pack()
	row_2_1 = Frame(lockers_2)
	row_2_1.pack()
	row_3_1 = Frame(lockers_2)
	row_3_1.pack()
	row_4_1 = Frame(lockers_2)
	row_4_1.pack()
	
	#--------------------------------------------------------------------------------
	
	btn13 = Button(row_1_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn13, 'Шкафчик №13', context))
	btn13.pack(side=LEFT)
	
	btn14 = Button(row_1_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn14, 'Шкафчик №14', context))
	btn14.pack(side=LEFT)
	
	btn15 = Button(row_1_1, text="Click Me", background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn15, 'Шкафчик №15', context))
	btn15.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn16 = Button(row_2_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn16, 'Шкафчик №16', context))
	btn16.pack(side=LEFT)
	
	btn17 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn17, 'Шкафчик №17', context))
	btn17.pack(side=LEFT)
	
	btn18 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn18, 'Шкафчик №18', context))
	btn18.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn19 = Button(row_3_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn19, 'Шкафчик №19', context))
	btn19.pack(side=LEFT)
	
	btn20 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn20, 'Шкафчик №20', context))
	btn20.pack(side=LEFT)
	
	btn21 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn21, 'Шкафчик №21', context))
	btn21.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn22 = Button(row_4_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn22, 'Шкафчик №22', context))
	btn22.pack(side=LEFT)
	
	btn23 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn23, 'Шкафчик №23', context))
	btn23.pack(side=LEFT)
	
	btn24 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn24, 'Шкафчик №24', context))
	btn24.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	
	lockers_3 = Frame(block_TOP)
	lockers_3.pack(side=LEFT)
	
	row_1_1 = Frame(lockers_3)
	row_1_1.pack()
	row_2_1 = Frame(lockers_3)
	row_2_1.pack()
	row_3_1 = Frame(lockers_3)
	row_3_1.pack()
	row_4_1 = Frame(lockers_3)
	row_4_1.pack()
	
	#--------------------------------------------------------------------------------
	
	btn25 = Button(row_1_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn25, 'Шкафчик №25', context))
	btn25.pack(side=LEFT)
	
	btn26 = Button(row_1_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn26, 'Шкафчик №26', context))
	btn26.pack(side=LEFT)
	
	btn27 = Button(row_1_1, text="Click Me", background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn27, 'Шкафчик №27', context))
	btn27.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn28 = Button(row_2_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn28, 'Шкафчик №28', context))
	btn28.pack(side=LEFT)
	
	btn29 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn29, 'Шкафчик №29', context))
	btn29.pack(side=LEFT)
	
	btn30 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn30, 'Шкафчик №30', context))
	btn30.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn31 = Button(row_3_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn31, 'Шкафчик №31', context))
	btn31.pack(side=LEFT)
	
	btn32 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn32, 'Шкафчик №32', context))
	btn32.pack(side=LEFT)
	
	btn33 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn33, 'Шкафчик №33', context))
	btn33.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn34 = Button(row_4_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn34, 'Шкафчик №34', context))
	btn34.pack(side=LEFT)
	
	btn35 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn35, 'Шкафчик №35', context))
	btn35.pack(side=LEFT)
	
	btn36 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn36, 'Шкафчик №36', context))
	btn36.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	
	lockers_4 = Frame(block_TOP, padx="10")
	lockers_4.pack(side=LEFT)
	
	row_1_1 = Frame(lockers_4)
	row_1_1.pack()
	row_2_1 = Frame(lockers_4)
	row_2_1.pack()
	row_3_1 = Frame(lockers_4)
	row_3_1.pack()
	row_4_1 = Frame(lockers_4)
	row_4_1.pack()
	
	#--------------------------------------------------------------------------------
	
	btn37 = Button(row_1_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn37, 'Шкафчик №37', context))
	btn37.pack(side=LEFT)
	
	btn38 = Button(row_1_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn38, 'Шкафчик №38', context))
	btn38.pack(side=LEFT)
	
	btn39 = Button(row_1_1, text="Click Me", background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn39, 'Шкафчик №39', context))
	btn39.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn40 = Button(row_2_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn40, 'Шкафчик №40', context))
	btn40.pack(side=LEFT)
	
	btn41 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn41, 'Шкафчик №41', context))
	btn41.pack(side=LEFT)
	
	btn42 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn42, 'Шкафчик №42', context))
	btn42.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn43 = Button(row_3_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn43, 'Шкафчик №43', context))
	btn43.pack(side=LEFT)
	
	btn44 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn44, 'Шкафчик №44', context))
	btn44.pack(side=LEFT)
	
	btn45 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn45, 'Шкафчик №45', context))
	btn45.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn46 = Button(row_4_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn46, 'Шкафчик №46', context))
	btn46.pack(side=LEFT)
	
	btn47 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn47, 'Шкафчик №47', context))
	btn47.pack(side=LEFT)
	
	btn48 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn48, 'Шкафчик №48', context))
	btn48.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	
	lockers_5 = Frame(block_TOP, padx="15")
	lockers_5.pack(side=LEFT)
	
	row_1_1 = Frame(lockers_5)
	row_1_1.pack()
	row_2_1 = Frame(lockers_5)
	row_2_1.pack()
	row_3_1 = Frame(lockers_5)
	row_3_1.pack()
	row_4_1 = Frame(lockers_5)
	row_4_1.pack()
	
	#--------------------------------------------------------------------------------
	
	btn49 = Button(row_1_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn49, 'Шкафчик №49', context))
	btn49.pack(side=LEFT)
	
	btn50 = Button(row_1_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn50, 'Шкафчик №50', context))
	btn50.pack(side=LEFT)
	
	btn51 = Button(row_1_1, text="Click Me", background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn51, 'Шкафчик №51', context))
	btn51.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn52 = Button(row_2_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn52, 'Шкафчик №52', context))
	btn52.pack(side=LEFT)
	
	btn53 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn53, 'Шкафчик №53', context))
	btn53.pack(side=LEFT)
	
	btn54 = Button(row_2_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn54, 'Шкафчик №54', context))
	btn54.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn55 = Button(row_3_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn55, 'Шкафчик №55', context))
	btn55.pack(side=LEFT)
	
	btn56 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn56, 'Шкафчик №56', context))
	btn56.pack(side=LEFT)
	
	btn57 = Button(row_3_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn57, 'Шкафчик №57', context))
	btn57.pack(side=LEFT)
	
	#--------------------------------------------------------------------------------
	
	btn58 = Button(row_4_1, image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn58, 'Шкафчик №58', context))
	btn58.pack(side=LEFT)
	
	btn59 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn59, 'Шкафчик №59', context))
	btn59.pack(side=LEFT)
	
	btn60 = Button(row_4_1, background="#555", image=photo, foreground="#ccc",
	             padx="20", pady="8", font="16", command=lambda:locker(btn60, 'Шкафчик №60', context))
	btn60.pack(side=LEFT)

	def status_check():
		""" БЛОК ОТРИСОВКИ АКТУАЛЬНОГО СОСТОЯНИЯ ОБЪЕКТА """
		
		btns = {btn :  'Шкафчик №1',  btn2: 'Шкафчик №2',   btn3: 'Шкафчик №3',   btn4: 'Шкафчик №4',
				btn5:  'Шкафчик №5',  btn6: 'Шкафчик №6',   btn7: 'Шкафчик №7',   btn8: 'Шкафчик №8',
				btn9:  'Шкафчик №9',  btn10: 'Шкафчик №10', btn11: 'Шкафчик №11', btn12: 'Шкафчик №12',
				btn13: 'Шкафчик №13', btn14: 'Шкафчик №14', btn15: 'Шкафчик №15', btn16: 'Шкафчик №16',
				btn17: 'Шкафчик №17', btn18: 'Шкафчик №18', btn19: 'Шкафчик №19', btn20: 'Шкафчик №20',
				btn21: 'Шкафчик №21', btn22: 'Шкафчик №22', btn23: 'Шкафчик №23', btn24: 'Шкафчик №24',
				btn25: 'Шкафчик №25', btn26: 'Шкафчик №26', btn27: 'Шкафчик №27', btn28: 'Шкафчик №28',
				btn29: 'Шкафчик №29', btn30: 'Шкафчик №30', btn31: 'Шкафчик №31', btn32: 'Шкафчик №32',
				btn33: 'Шкафчик №33', btn34: 'Шкафчик №34', btn35: 'Шкафчик №35', btn36: 'Шкафчик №36',
				btn37: 'Шкафчик №37', btn38: 'Шкафчик №38', btn39: 'Шкафчик №39', btn40: 'Шкафчик №40',
				btn41: 'Шкафчик №41', btn42: 'Шкафчик №42', btn43: 'Шкафчик №43', btn44: 'Шкафчик №44',
				btn45: 'Шкафчик №45', btn46: 'Шкафчик №46', btn47: 'Шкафчик №47', btn48: 'Шкафчик №48',
				btn49: 'Шкафчик №49', btn50: 'Шкафчик №50', btn51: 'Шкафчик №51', btn52: 'Шкафчик №52',
				btn53: 'Шкафчик №53', btn54: 'Шкафчик №54', btn55: 'Шкафчик №55', btn56: 'Шкафчик №56',
				btn57: 'Шкафчик №57', btn58: 'Шкафчик №58', btn59: 'Шкафчик №59', btn60: 'Шкафчик №60'}
		
		for i in btns: # Передача списка шкафчиков в функцию статуса
			name = btns.get(i)
			stat(i, name, context)


	status_check()
	#--------------------------------------------------------------------------------
# rendering_lockers(root)
