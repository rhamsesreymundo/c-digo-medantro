from tkinter import *
import os

class Medantro():
    def _init_(self):
        root=Tk()
        self.bmedicion=Button(root, text = "Medición", command=self.medir3)
        self.bmedicion.pack()
        self.can1=Canvas(root, width = 520, height = 700, bg="#26ff00")
        self.can1.pack()
        self.lst=[]
        self.lstx=[]
        self.lsty=[]
        img = PhotoImage(file="altura.PNG")
        self.can1.create_image(20, 20, anchor=NW, image=img)
        self.cont=1
        self.can1.bind("<ButtonRelease-1>", self.medir1)
        self.can1.bind("<B1-Motion>", self.medir2)
        
        self.uni=0
        self.med=0
        self.medr=0
        root.mainloop()
    def medir1(self, event):
        x = event.x
        y = event.y

        self.can1.create_line(x, y, 0, y, fill="#26ff00", tags= "nline")
        self.can1.create_line(x, y, x, 0, fill="#26ff00", tags= "nline")
        self.can1.create_line(x, y, x, 700, fill="#26ff00", tags= "nline")
        self.can1.create_line(x, y, 520, y, fill="#26ff00", tags= "nline")
        
        if self.cont <= 2:   
            self.cont += 1
            self.lstx.append(x)
            self.lsty.append(y)
            if len(self.lstx)==2:
                self.unix=abs(self.lstx[1]-self.lstx[0])
                self.uniy=abs(self.lsty[1]-self.lsty[0])
                
            
                self.uni=((self.unix)*2+(self.uniy)2)*0.5
                print("1 metro equivale a: ",self.uni)
            print("Eje x ", self.lstx)
            print("Eje y ", self.lsty)
        else:
            self.lstx.append(x)
            self.lsty.append(y)
            print("Eje x ", self.lstx)
            print("Eje y ", self.lsty)
            self.cont += 1

    def medir2(self, event):
        self.can1.delete("line")
        
        x = event.x
        y = event.y

        self.can1.create_line(x, y, 0, y, fill="gray", tags= "line")
        self.can1.create_line(x, y, x, 0, fill="gray", tags= "line")
        self.can1.create_line(x, y, x, 700, fill="gray", tags= "line")
        self.can1.create_line(x, y, 520, y, fill="gray", tags= "line")

        self.can1.update()
        self.can1.after(50)
        
    def medir3(self):
        self.medx=abs(self.lstx[len(self.lstx)-1] - self.lstx[len(self.lstx)-2])
        self.medy=abs(self.lsty[len(self.lsty)-1] - self.lsty[len(self.lsty)-2])
        self.med=((self.medx)*2+(self.medy)2)*0.5
        self.medr=(self.med)/self.uni
        print(self.medr)
        



Medantro()
