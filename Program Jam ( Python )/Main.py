from tkinter import *
import time

 


class Jam:
    def __init__(self, parent):
        self.parent = parent
        self.komponen()
        self.refresh()

    def komponen(self):
        self.teksJam = StringVar()
        
        self.teks = Label(text="Jam Onii-Chan", font =('Harvetica', 10, 'bold'), bg ="white", fg= "grey")
        self.teks.pack()

        layarJam = Frame(self.parent, bd=10, bg="black")
        layarJam.pack()

        self.jam = Label(layarJam, textvariable=self.teksJam,font=('Halvetica', 50, 'bold'),bg = "black",fg="white")
        self.jam.pack()
        
       

    def refresh(self):
        datJam = time.strftime("%H:%M:%S", time.localtime())

        self.teksJam.set(datJam)
        self.timer = self.parent.after(1000, self.refresh)
    

        



if __name__ == '__main__':
    root = Tk()
    root.title("Clock")
    app = Jam(root)
    root.mainloop()