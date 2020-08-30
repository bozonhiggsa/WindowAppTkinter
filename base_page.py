from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
from PIL import ImageTk, Image

def clicked1():
     res = "Привет {}".format(txt.get())
     lbl.configure(text=res)
def clicked2():
     res = combo.get()
     if res.isdecimal():
         lb2.configure(text=int(res)*10)
     else:
         messagebox.showwarning('Ошибка ввода', 'Параметр должен быть целым числом')

def clicked3():
    res1 = chk_state1.get()
    res2 = chk_state2.get()
    lb3.configure(text=str(res1) + ', ' + str(res2))
def clicked4():
    lb4.configure(text=selected.get())
def clicked5():
    file = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg"), ("all files", "*.*")))
    lb6.configure(text=file)
    picture = Toplevel()
    picture.title("Изображение")
    picture.configure(background='grey')
    load = Image.open(file)
    # load = Image.open("example1.jpg")
    img = ImageTk.PhotoImage(load)
    label = Label(picture, image=img)
    label.pack()
    picture.mainloop()
def clicked6():
     value = slider.get()
     lb5.configure(text=value)

window = Tk()
window.title("Добро пожаловать в приложение Python")
window.geometry('800x600')
lbl = Label(window, text="Привет", font=("Arial Bold", 30))
lbl.place(x=20, y=20)
# lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.focus()
txt.place(x=400, y=40)
# txt.grid(column=1, row=0)
btn = Button(window, text="Клик!", command=clicked1, bg="black", fg="red")
btn.place(x=480, y=35)
# btn.grid(column=2, row=0)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(0)  # установите вариант по умолчанию
combo.place(x=20, y=100)
# combo.grid(column=0, row=1)
btn2 = Button(window, text="Клик!", command=clicked2, bg="yellow", fg="black")
btn2.place(x=180, y=98)
# btn2.grid(column=1, row=1)
lb2 = Label(window, text="Вывод из combo", font=("Arial Bold", 20))
lb2.place(x=250, y=92)
# lb2.grid(column=2, row=1)

chk_state1 = BooleanVar()
chk_state1.set(True)
chk1 = Checkbutton(window, text='Выбрать', var=chk_state1)
chk1.place(x=20, y=200)
#chk1.grid(column=0, row=2)
chk_state2 = IntVar()
chk_state2.set(1)
chk2 = Checkbutton(window, text='Выбрать', var=chk_state2)
chk2.place(x=110, y=200)
#chk2.grid(column=1, row=2)
btn3 = Button(window, text="Клик!", command=clicked3, bg="yellow", fg="black")
btn3.place(x=200, y=200)
#btn3.grid(column=2, row=2)
lb3 = Label(window, text="Вывод из checkbuttons", font=("Arial Bold", 10))
lb3.place(x=260, y=202)
#lb3.grid(column=3, row=2)

selected = IntVar()
selected.set(2)
rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)
rad1.place(x=20, y=300)
#rad1.grid(column=0, row=3)
rad2.place(x=100, y=300)
#rad2.grid(column=1, row=3)
rad3.place(x=180, y=300)
#rad3.grid(column=2, row=3)
btn4 = Button(window, text="Клик!", command=clicked4, bg="yellow", fg="black")
btn4.place(x=260, y=299)
#btn4.grid(column=3, row=3)
lb4 = Label(window, text="Вывод из radiobuttons", font=("Arial Bold", 10))
lb4.place(x=320, y=301)
#lb4.grid(column=4, row=3)

slider = Scale(window, orient=HORIZONTAL, length=300, from_=0, to=100, tickinterval=10, resolution=1)
slider.place(x=40, y=400)
btn5 = Button(window, text="Клик!", command=clicked6, bg="yellow", fg="black")
btn5.place(x=380, y=416)
lb5 = Label(window, text="Вывод из слайдера", font=("Arial Bold", 10))
lb5.place(x=440, y=417)

menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Открыть файл', command=clicked5)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
lb6 = Label(window, text="Open file", font=("Arial Bold", 10))
lb6.place(x=20, y=500)
# lb5.grid(column=0, row=4)

window.mainloop()

