from tkinter import *
from tkinter import messagebox, filedialog


# Функция смены тем редактора
def change_theme(theme):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']


# Функция смены шрифтов редактора
def change_fonts(selfont):
    text_field['font'] = fonts[selfont]['font']


# Функция закрытия текстового редактора
def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()


# Функция открытия файла в текстовом редакторе
def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'),
                                                                           ('Все файлы', '*.*')))
    if file_path:
        text_field.delete(1.0, END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())


# Функция сохранения файла
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'),
                                                                           ('Все файлы', '*.*')),
                                             defaultextension='*.txt')
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()

# Создание основного окна TKinter
root = Tk()
# Добавление заголовка окна
root.title('Текстовый редактор')
# Установка разрешения окна редактора
root.geometry('600x700')

# добавляем главное меню
main_menu = Menu(root)
# Пункт меню "Файл"
file_menu = Menu(main_menu, tearoff=0) # tearoff=0 убирает пунктирную линию по умолчанию для меню в TKinter
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
# добавление линии-разделителя
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

# Пункт меню "Вид"
view_menu = Menu(main_menu, tearoff=0)
# Подкатегория меню "Вид"
view_menu_sub = Menu(view_menu, tearoff=0)
# Подкатегория меню "Шрифт"
font_menu_sub = Menu(view_menu, tearoff=0)
# Добавление списка подкатегории меню "Вид"
view_menu_sub.add_command(label="Тёмная", command=lambda: change_theme('dark'))
view_menu_sub.add_command(label="Светлая", command=lambda: change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)
# Добавление списка подкатегории меню "Шрифт"
font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('TNR'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)
# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)


# Добавляем фрейм для текста
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)
# добавление переключения тем редактора
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}
# добавление переключения шрифтов
fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}

# Добавляем виджет текстового поля
# тёмная (ночная) тема (по умолчанию)
text_field = Text(f_text,
                  bg='black', # цвет фона окна редактора
                  fg='lime',  # цвет текста окна редактора
                  padx=10,    # отступ слева
                  pady=10,     # отступ справа
                  wrap=WORD,    # перенос текста
                  insertbackground='brown', # добавление курсора
                  selectbackground='#8D917A', # добавление выделения текста
                  spacing3=10, # добавление абзацного отступа
                  width=30, # ширина текста
                  font='Arial 14 bold'
                  )
# отбражение текстового поля(виджет) на экране
text_field.pack(expand=1, fill=BOTH, side=LEFT)

# добавление полосы прокрутки (виджет)
scroll = Scrollbar(f_text, command=text_field.yview)
# отбражение полосы прокрутки (виджет) на экране
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)



# Запуск окна
root.mainloop()