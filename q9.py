from tkinter import * 
window=Tk() 
window.geometry('200x200') 
window.title('9. Calculator') 
window.configure(bg='black') 
text=StringVar() 
listval=[] def click_1(): text.set('1') 
listval.append(1) def click_2(): text.set('2') 
listval.append(2) def click_3(): text.set('3') 
listval.append(3) def click_4(): 
text.set('4') listval.append(4) def 
click_5(): text.set('5') 
listval.append(5) def click_6(): 
text.set('6') listval.append(6) def 
click_7(): text.set('7') 
listval.append(7) def click_8(): 
text.set('8') listval.append(8) def 
click_9(): text.set('9') 
listval.append(8) def click_0(): 
text.set('0')
listval.append(9)
def click_plus(): 
text.set('+') 
listval.append('+') def 
click_minus(): 
text.set('-') 
listval.append('-') def 
click_div(): 
text.set('/') 
listval.append('/') def 
click_mult(): 
text.set('*') 
listval.append('*') def 
click_pow(): 
text.set('^') 
listval.append('^') def 
click_mod(): 
text.set('%')
listval.append('%')
def click_result(): 
ans=0
if(listval[1]=="+"):
ans+=(listval[0]+listval[2]) 
elif(listval[1]=="-"):
ans+=(listval[0]-listval[2]) 
elif(listval[1]=="/"):
ans+=(listval[0]/listval[2]) 
elif(listval[1]=="*"):
ans+=(listval[0]*listval[2]) 
elif(listval[1]=="^"):
ans+=(listval[0]**listval[2]) 
elif(listval[1]=="%"):
ans+=(listval[0]%listval[2])
for i in range(3,len(listval)): 
if(listval[i]=='+'):
ans+=listval[i+1] 
elif(listval[i]=='-'): ans-
=listval[i+1] elif(listval[i]=='*'):
ans*=listval[i+1] 
elif(listval[i]=='/'):
ans/=listval[i+1] 
elif(listval[i]=='^'):
ans**=listval[i+1] 
elif(listval[i]=='%'):
ans%=listval[i+1] 
text.set(str(ans))
CalculatorDisplay=Label(window,textvariable=text,width=10,height=1,bg='white').grid(row=0,column=1
) le=Label(window,bg="black").grid(row=1,column=0) 
b1=Button(window,text='1',command=click_1,width=7,height=1,bg='white',activebackground='red').gri 
d(row=3,column=0) 
b2=Button(window,text='2',command=click_2,width=7,height=1,bg='white',activebackground='red').gri 
d(row=3,column=1) 
b3=Button(window,text='3',command=click_3,width=7,height=1,bg='white',activebackground='red').gri 
d(row=4,column=0) 
b4=Button(window,text='4',command=click_4,width=7,height=1,bg='white',activebackground='red').gri 
d(row=4,column=1) 
b5=Button(window,text='5',command=click_5,width=7,height=1,bg='white',activebackground='red').gri 
d(row=5,column=0) 
b6=Button(window,text='6',command=click_6,width=7,height=1,bg='white',activebackground='red').gri 
d(row=5,column=1) 
b7=Button(window,text='7',command=click_7,width=7,height=1,bg='white',activebackground='red').gri 
d(row=6,column=0) 
b8=Button(window,text='8',command=click_8,width=7,height=1,bg='white',activebackground='red').gri 
d(row=6,column=1) 
b9=Button(window,text='9',command=click_9,width=7,height=1,bg='white',activebackground='red').gri 
d(row=7,column=0)
b0=Button(window,text='0',command=click_0,width=7,height=1,bg='white',activebackground='red').gri 
d(row=7,column=1)
b_plus=Button(window,text='+',command=click_plus,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=2,column=2) 
b_minus=Button(window,text='-',command=click_minus,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=3,column=2) 
b_div=Button(window,text='/',command=click_div,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=4,column=2) 
b_mult=Button(window,text='*',command=click_mult,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=5,column=2) 
b_equal=Button(window,text='=',command=click_result,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=6,column=2) 
b_pow=Button(window,text='^',command=click_pow,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=7,column=2) 
b_mod=Button(window,text='%',command=click_mod,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=2,column=1)
b_close=Button(window,text='close',command=window.destroy,width=7,height=1,bg='light 
grey',activebackground='red').grid(row=2,column=0) window.mainloop()
