from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


window = Tk()

Hintergrund= PhotoImage(file= "Hintergrund.png")
window.geometry("600x600")
window.title("Monopoly")

def Button_action():
    feld=Tk()
    feld_button = Button(feld, text="test", command=feld.destroy)
    feld_button.place(x= 225, y=200, width=160, height=120)
    feld.geometry("600x600")
    feld.title("feld")

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open("Hintergrund.png")
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

start_button = Button(window, text="START", command=lambda: [Button_action(), window.destroy()])
exit_button = Button(window, text="Beenden", command=window.quit)


exit_button.place(x = 225, y = 400,width=160, height=120)
start_button.place(x = 225, y = 200,width=160, height=120)


window.mainloop()
