import tkinter
import qrcode
from PIL import ImageTk, Image

def clicked():
    path = 'qr.png'  # путь к файлу с qr кодом
    # Для начала создадим qr code
    qr = qrcode.QRCode(
        version=3,  # плотность точек
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,  # размеры изображения
        border=4  # ширина бордюра по умолчанию равен 4
    )
    link = txt.get()
    qr.add_data(link)
    qr.make(fit=True)

    # сохраним qr код в файл
    img = qr.make_image()
    img.save('qr.png')

    # откроем qr код из файла
    img = ImageTk.PhotoImage(Image.open(path))
    panel.config(image=img)  # обновляем изображение
    panel.photo_ref = img  # сохраняем ссылку на изображение (обязательно!)
    root.update_idletasks()

    
root = tkinter.Tk()
root.title('Qr Code')
root.geometry('300x300')
root.resizable(0, 0)

lbl = tkinter.Label(root, text='Введите адрес сайта:', width=40, border=1)
txt = tkinter.Entry(root, width=40, border=1)
btn = tkinter.Button(root, text='Сгенерировать Qr код', command=clicked, border=1)
panel = tkinter.Label(root)

#panel.pack(side = "bottom", fill = "both", expand = "yes")

lbl.pack()
txt.pack()
btn.pack()
panel.pack()

root.mainloop()


