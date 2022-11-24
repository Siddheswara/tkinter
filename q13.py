from tkinter import *
import tkinter.ttk as ttk
window=Tk()
window.title('13. Bookstore Management Software by A') 
window.geometry('1400x500') 
window.configure(bg="light grey") 
le=Label(window,width=5,bg='light grey').grid(row=0,column=0) 
l1=Label(window,text='Title',bg='light grey').grid(row=0,column=1) 
e1=Entry(window).grid(row=0,column=2) 
le=Label(window,width=5,bg='light grey').grid(row=0,column=3) 
l2=Label(window,text='Author',bg='light grey').grid(row=0,column=4) 
e2=Entry(window).grid(row=0,column=5) 
l3=Label(window,text='Year',bg='light grey').grid(row=1,column=1) 
e3=Entry(window).grid(row=1,column=2) 
l4=Label(window,text='ISBN',bg='light grey').grid(row=1,column=4)
e4=Entry(window).grid(row=1,column=5) 
le=Label(window,bg='light grey').grid(row=2,column=0)
s = ttk.Style() 
s.theme_use('clam')
s.configure('Treeview.Heading', background="light grey") 
tree=ttk.Treeview(window, 
column=("c1", "c2","c3","c4","c5"), show= 'headings', height= 10) 
tree.grid(row=3,column=3) 
tree.heading("# 1", text= "ID") 
tree.heading("# 2", text= "Title") 
tree.heading("# 3", text= "Author") 
tree.heading("# 4", text= "Year") 
tree.heading("# 5", text= "ISBN") 
tree.insert('', 'end',text= "1",values=('1','The Earth','Monkee','2012','458735754837'))
tree.insert('', 'end',text= "2",values=('2','The Moon','Itachi','2016','984589745888')) 
le=Label(window,bg='light grey').grid(row=4,column=0) 
b1=Button(window,text="View All",bg="light grey",activebackground='orange').grid(row=5,column=3) 
b2=Button(window,text="Search",bg="light grey",activebackground='orange').grid(row=6,column=3) 
b3=Button(window,text="Add Entry",bg="light grey",activebackground='orange').grid(row=7,column=3) 
b4=Button(window,text="Update Selected",bg="light grey",activebackground='orange').grid(row=8,column=3) 
b5=Button(window,text="Delete Selected",bg="light grey",activebackground='orange').grid(row=9,column=3) 
b6=Button(window,text="Close",command=window.destroy,bg="light grey",activebackground='orange').grid(row=10,column=3) 
window.mainloop()