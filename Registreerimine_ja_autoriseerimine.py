from multiprocessing.connection import wait
from tkinter import *
from math import *

paroolid=['1234']
sisselogimised=['']



def Registreerimine():
    if ent.get()=="": 
        ent.configure(bg="red")
    else:
        ent.configure(bg="lightblue")
    if ent1.get()=="": 
        ent1.configure(bg="red")
    else:
        ent1.configure(bg="lightblue")
    if ent.get()!='' and ent1.get()!='':
        if ent.get() not in sisselogimised:
            sisselogimised.append(ent.get())
            if ent1.get() not in sisselogimised:
                paroolid.append(ent1.get())
                aken=Tk()
                aken.geometry("400x100")
                aken.title("Registreerimine ja autoriseerimine")
                lbl=Label(aken,text="Sa oled registreerusid",font="Times 20", fg="green",bg="lightblue")
                lbl.pack()
                btn=Button(aken,text="Sulge aken", font="Times 20",bg="lightblue",fg="green",command=lambda: aken.destroy())
                btn.pack()
                aken.mainloop()

def rparool():
    import random
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    print(psword)

def Autoriseerimine():
    if ent.get()=="": 
        ent.configure(bg="red")
    else:
        ent.configure(bg="lightblue")
    if ent1.get()=="": 
        ent1.configure(bg="red")
    else:
        ent1.configure(bg="lightblue")
    if ent.get()!='' and ent1.get()!='':
        if ent.get() not in sisselogimised:
            ent.get().config(text='Vale hüüdnimi')
        if ent1.get() not in sisselogimised:
            aken=Tk()
            aken.geometry("400x100")
            aken.title("Registreerimine ja autoriseerimine")
            lbl=Label(aken,text="Sa oled autoriseeritud",font="Times 20", fg="green",bg="lightblue")
            lbl.pack()
            btn=Button(aken,text="Sulge aken", font="Times 20",bg="lightblue",fg="green",command=lambda: aken.destroy())
            btn.pack()
            aken.mainloop()

def muutmine():
    aken=Tk()
    aken.geometry("500x400")
    aken.title("Registreerimine ja autoriseerimine")
    lbl=Label(aken,text="sisestage oma vana parool või hüüdnimi",font="Times 20", fg="green",bg="lightblue")
    lbl.pack()
    q=Entry(aken,font="Times 20", fg="black",bg="lightblue",width=15)
    q.pack()
    btn=Button(aken,text="läbivaatus", font="Times 20",bg="lightblue",fg="green",)
    btn.pack()
    if q.get()!='':
        if paroolid.index(q.get()) in paroolid:
            paroolid.index(q.get()).pop()
            lbl=Label(aken,text="sisestage oma uue parool või hüüdnimi",font="Times 20", fg="green",bg="lightblue")
            lbl.pack()
            w=Entry(aken,font="Times 20", fg="black",bg="lightblue",width=15)
            w.pack()
            if w.get()!='':
                if paroolid.index(w.get()) in paroolid:
                    lbl1=Label(aken,text="Hüüdnimi",font="Times 20", fg="green",bg="lightblue")
                    lbl1.config(text='See parool on juba olemas')
                    lbl1.pack(side=BOTTOM)
                else:
                    paroolid.index(w.get()).append(paroolid)
                    print(paroolid)
                    aken.mainloop()

def parooli_taastamine():
    aken=Tk()
    aken.geometry("500x400")
    aken.title("Registreerimine ja autoriseerimine")
    lbl=Label(aken,text="sisestage hüüdnimi",font="Times 20", fg="green",bg="lightblue")
    lbl.pack()
    q=Entry(aken,font="Times 20", fg="black",bg="lightblue",width=15)
    q.pack()
    if q.get()=='':
        if sisselogimised.index(q.get()) in paroolid:
            lbl1=Label(aken,text=f'Teie parool on {sisselogimised.index(q.get())}',font="Times 20", fg="green",bg="lightblue")
            lbl1.pack()

aken=Tk()
aken.geometry("700x500")
aken.title("Registreerimine ja autoriseerimine")
aken.config(cursor="watch")


lbl=Label(aken,text="Hüüdnimi",font="Times 20", fg="green",bg="lightblue")
lbl.pack()

ent=Entry(aken,font="Times 20", fg="black",bg="lightblue",width=15)
ent.pack()

lbl1=Label(aken,text="Parool",font="Times 20", fg="green",bg="lightblue")
lbl1.pack()

ent1=Entry(aken,font="Times 20", fg="black",bg="lightblue",width=15)
ent1.pack()

btn=Button(aken,text="Registreerimine", font="Times 20",bg="lightblue",fg="green",command=Registreerimine)
btn.pack()

btn1=Button(aken,text="Autoriseerimine", font="Times 20",bg="lightblue",fg="green",command=Autoriseerimine)
btn1.pack()

btn2=Button(aken,text="Random parool", font="Times 20",bg="lightblue",fg="green",command=rparool)
btn2.pack()

btn3=Button(aken,text="Nime või parooli muutmine", font="Times 20",bg="lightblue",fg="green",command=muutmine)
btn3.pack()

btn4=Button(aken,text="Unustanud parooli taastamine", font="Times 20",bg="lightblue",fg="green",command=parooli_taastamine)
btn4.pack()

aken.mainloop()