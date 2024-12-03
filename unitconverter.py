import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.geometry("300x300")
str=""
def confirm(event):
    if cb3.get()=="Temperature":
       cb2['values']=("Celsius","Fahrenheit","Kelvin")
       cb2.update()
       cb1['values']=("Celsius","Feranheit","Kelvin")
       cb1.update()
    elif cb3.get()=="Lenght":
       cb2['values']=("KM","CM","METER","FEET")
       cb2.update()
       cb1['values']=("KM","CM","METER","FEET")
       cb1.update()
    else:
       cb2['values']=("Dollar","Rupess","Euro","Pound")
       cb2.update()
       cb1['values']=("Dollar","Rupess","Euro","Pound")
       cb1.update()
def clearmy():
    global str
    e.set("")
    str=""

def click(my):
    global str
    str=str+my
    e.set(str)
def back():
    global str
    str=str[0:len( str)-1]
    e.set(str)    
def convert():
    if cb1.get()=='KM':
        if cb2.get()=='METER':
            value=int(b1.get())
            result.set(value*1000)
        elif cb2.get()=='CM':
            value=int(b1.get())
            result.set(value*100000)
        elif cb2.get()=='Feet':
            value=int(b1.get())
            result.set(value*3280.84)
        elif cb2.get()=='KM':
            value=int(b1.get())
            result.set(value)
    if cb1.get()=="METER":
        if cb2.get()=="KM":
            value=int(b1.get())
            result.set(value/1000)
        elif cb2.get()=="CM":
            value=int(b1.get())
            result.set(value*100)
        elif cb2.get()=="FEET":
            value=int(b1.get())
            result.set(value*3.28084)
        elif cb2.get()=="METER":
            value=int(b1.get())
            result.set(value)
    if cb1.get()=="CM":
        if cb2.get()=="KM":
            value=int(b1.get())
            result.set(value/100000)
        elif cb2.get()=="CM":
            value=int(b1.get())
            result.set(value)
        elif cb2.get()=="FEET":
            value=int(b1.get())
            result.set(value/30.48)
        elif cb2.get()=="METER":
            value=int(b1.get())
            result.set(value/100)
    if cb1.get()=="FEET":
        if cb2.get()=="KM":
            value=int(b1.get())
            result.set(value/3280.84)
        elif cb2.get()=="CM":
            value=int(b1.get())
            result.set(value*30)
        elif cb2.get()=="FEET":
            value=int(b1.get())
            result.set(value)
        elif cb2.get()=="METER":
            value=int(b1.get())
            result.set(value/3.28084)
    if cb1.get()=="Celsius":
        if cb2.get()=="Feranheit":
            value=int(b1.get())
            result.set((value*9/5)+32)
        elif cb2.get()=="Kelvin":
            value=int(b1.get())
            result.set(value+273.15)
    if cb1.get()=="Feranheit":
        if cb2.get()=="Celsius":
            value=int(b1.get())
            result.set((value-32)*5/9)
        elif cb2.get()=="Kelvin":
            value=int(b1.get())
            result.set((value+459.67)*5/9)
    if cb1.get()=="Kelvin":    
        if cb2.get()=="Celsius":            
            value=int(b1.get())
            result.set((value-273.15))
        elif cb2.get()=="Feranheit":               
            value=int(b1.get())
            result.set((value-273.15)*9/5+32)
    if cb1.get()=="Dollar":
        if cb2.get()=="Rupess" :
            value=int(b1.get())
            result.set((value*83.40))
        elif cb2.get()=="Euro":
            value=int(b1.get())
            result.set((value*0.93))
        elif cb2.get()=="Pound":
            value=int(b1.get())
            result.set((value*0.80))
            
    
            
            
#entry=tk.Entry(root,width=20).grid(column=3,row=1)
f=tk.Frame()
a1=tk.Label(f,text="Select Type of unit")
a1.pack(side="left")
cb3=ttk.Combobox(f)
cb3['values']=("Lenght","Temperature","Currency")
cb3.bind("<<ComboboxSelected>>",confirm)
cb3.pack(side="left")
#tk.Button(f,text="Confirm",command=confirm).pack(side="left")
f.pack()
f=tk.Frame()
a=tk.Label(f,text="Unit1")
a.pack(side="left")
cb1=ttk.Combobox(f)

cb1.pack(side="left")
b=tk.Label(f,text="covert to")
b.pack(side="left")

cb2=ttk.Combobox(f)
cb2.pack(side="left")
f.pack()
            
f=tk.Frame()
b=tk.Label(f,text="enter value")
b.pack(side="left")
e=tk.IntVar()
b1=tk.Entry(f,textvariable=e,fg="blue")
b1.pack(side="left")
b=tk.Button(f,text="covert",command=convert)
b.pack(side="left")
result=tk.StringVar()
out=tk.Label(f,textvariable=result)
out.pack(side="left")
f.pack()
f=tk.Frame()
b=tk.Button(f,text="1",fg="white",bg="grey",font="arial,35,bold",
             height=2,width=10,command=lambda:click("1"))
b.pack(side="left")
b=tk.Button(f,text="2",fg="white",bg="grey",font="arial,35,bold",
             height=2,width=10,command=lambda:click("2"))
b.pack(side="left")
b=tk.Button(f,text="3",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("3"))
b.pack(side="left")
f.pack()

f=tk.Frame()
b=tk.Button(f,text="4",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("4"))
b.pack(side="left")
b=tk.Button(f,text="5",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("5"))
b.pack(side="left")
b=tk.Button(f,text="6",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("6"))
b.pack(side="left")
f.pack()
f=tk.Frame()
b=tk.Button(f,text="7",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("7"))
b.pack(side="left")
b=tk.Button(f,text="8",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("8"))
b.pack(side="left")
b=tk.Button(f,text="9",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("9"))
b.pack(side="left")
f.pack()
f=tk.Frame()
b=tk.Button(f,text="0",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=lambda:click("0"))
b.pack(side="left")
b=tk.Button(f,text="<-",fg="white",bg="grey",font="arial,35,bold",
              height=2,width=10,command=back)
b.pack(side="left")
b=tk.Button(f,text="c",fg="white",bg="pink",font="arial,35,bold",
             height=2,width=10,command=clearmy)
b.pack(side="left")
f.pack()


root.mainloop()
