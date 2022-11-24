from ctypes.wintypes import INT
from tkinter import *
window=Tk()
window.title('12. Python Guides') 
window.configure(bg="light grey")
le=Label(window,bg="light grey",width=5).grid(row=0,column=0) 
l1=Label(window,text='FullName:').grid(row=0,column=1) 
e1=Entry(window).grid(row=0,column=2) 
l2=Label(window,text='Email : ').grid(row=1,column=1) 
e2=Entry(window).grid(row=1,column=2) 
l3=Label(window,text='Password:').grid(row=2,column=1) 
e3=Entry(window,show="*").grid(row=2,column=2) 
le=Label(window,bg="lightgrey").grid(row=3,column=0) 
l4=Label(window,text="Gender").grid(row=4,column=1)
var1=INT
var2=INT
rb1=Radiobutton(window,text='Female',bg='light grey',variable=var1,value=1).grid(row=4,column=2) 
rb2=Radiobutton(window,text='Male ',bg='light grey',variable=var1,value=2).grid(row=5,column=2) 
rb3=Radiobutton(window,text='Others',bg='light grey',variable=var1,value=3).grid(row=6,column=2) 
le=Label(window,bg="light grey").grid(row=8,column=0) 
chkb=Checkbutton(window,text='Accept the terms &conditions',variable=var2,onvalue=1,offvalue=0).grid(row=9,column=2) 
le=Label(window,bg="light grey").grid(row=10,column=0) 
b=Button(window,text='Submit').grid(row=11,column=2) 
window.mainloop()