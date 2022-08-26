import tkinter as tk
import tkinter.filedialog as fd
import pytesseract
import os
from PIL import Image, ImageTk
import win32api
import tkinter

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(width=False, height=False)
        self.geometry('1200x720')
        self.title('Средство идентификации финансовых документов')
        self.image = tk.PhotoImage(file='C:\\sourceprog\\phon.png')
        bg_logo = tk.Label(self, image=self.image)
        bg_logo.place(x=0, y=0, relwidth=1, relheight=1)
        butt = tk.Button(self, text= 'ВЫБРАТЬ ФАЙЛ', bg='#25609a', fg='#ffffff', font='gilroy', command=self.choose_file)
        butt.place(x=116, y=362)
        

        



    def choose_file(self):
        filetypes = (("Изображение", "*.jpg *.png *.tiff"),
                     ("Текстовый файл", "*.txt"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)


        
        img = Image.open(filename)
        file_name = img.filename
        file_name = file_name.split(".")[0]
        oplata = 0
        faktura = 0
        text = pytesseract.image_to_string(img, lang='rus').strip()
        if text.find("Продавец") != -1:
            faktura = faktura + 1
        if text.find("Адрес") != -1:
            faktura = faktura + 1
        if text.find("К платежно-расчетному документу") != -1:
            faktura = faktura + 2
        if text.find("Валюта") != -1:
            faktura = faktura + 1
        if text.find("Идентификатор государственного контракта") != -1:
            faktura = faktura + 1
        if text.find("Приложение") != -1:
            faktura = faktura + 1
        if text.find("к постановлению Правительства Российской Федерации") != -1:
            faktura = faktura + 3
        if text.find("Наименование товара") != -1:
            faktura = faktura + 1
        if text.find("Код") != -1:
            faktura = faktura + 1
        if text.find("Российский рубль, 643") != -1:
            faktura = faktura + 2
        if text.find("национальное") != -1:
            faktura = faktura + 1
        if text.find("измерения") != -1:
            faktura = faktura + 1
        if text.find("ставка") != -1:
            faktura = faktura + 1
        if text.find("таможенной") != -1:
            faktura = faktura + 1
        if text.find("декларации") != -1:
            faktura = faktura + 1
        if text.find("Акт") != -1 or text.find("АКТ") != -1:
            faktura = faktura - 2
        if text.find("КОНТРАКТ") != -1 or text.find("АКТИВ") != -1 or text.find("Актив") != -1:
            faktura = faktura + 2
        if faktura > 3:
            win32api.MessageBox(0, 'Счет-фактура', 'Документ распознан')
        else:
            if text.find("Счет") != -1:
                win32api.MessageBox(0, 'Счет на оплату', 'Документ распознан')
            else:
                if text.find("Банк") != -1:
                    oplata = oplata + 1
                if text.find("БИК") != -1:
                    oplata = oplata + 2
                if text.find("Основание") != -1:
                    oplata = oplata + 1
                if text.find("Товары") != -1:
                    oplata = oplata + 1
                if text.find("Гражданско-правовой договор") != -1:
                    oplata = oplata + 2
                if text.find("Товар") != -1:
                    oplata = oplata + 1
                if text.find("товара") != -1:
                    oplata = oplata + 1
                if text.find("Итого") != -1:
                    oplata = oplata + 1
                if (text.find("Акт") != -1 or text.find("АКТ") != -1) and text.find("Гражданско-правовой договор") != -1:
                    oplata = oplata - 5
                elif (text.find("Акт") != -1 or text.find("АКТ") != -1) and text.find("Гражданско-правовой договор") == -1:
                    oplata = oplata - 2
                if text.find("КОНТРАКТ") != -1 or text.find("АКТИВ") != -1 or text.find("Актив") != -1:
                    oplata = oplata + 2
                    if text.find("Гражданско-правовой договор") != -1:
                        oplata = oplata + 3
                if oplata > 2:
                    win32api.MessageBox(0, 'Счет на оплату', 'Документ распознан')
                else:
                    win32api.MessageBox(0, 'Ошибка', 'Документ распознан')
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
