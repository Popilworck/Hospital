from pathlib import Path
import os,dbms as d
from tkinter import messagebox
import main_
from tkinter import *
from tkinter import ttk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{os.getcwd()}\docmenu\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
fonts = lambda a:("Inter ExtraBold", a * -1,'bold')
x1=1536#x resolution
y1=888#y resolution
o = lambda a: a/x1
p= lambda a:a/y1
def x():messagebox.showerror("ERROR", "INVALID INPUT, PLEASE RE-ENTER")
def dest(l=['mylist','sb','pat_name_label','pat_name_entry','button_6','label1','button_7','text_1','sb2','pat_name_entry2','pat_name_label2']):
        for i in l:
            try:
                exec(f'{i}.destroy()')
            except:pass
def main(sid):
    window = Tk() 
    window.bind('<Escape>',lambda a:window.destroy())
    def lo():
        window.destroy()
        main_.start()
    sname = d.idtoname(s=sid)
    global sb2
    global mylist,sb,pat_name_entry,pat_name_label,button_6,pat_name_label2,pat_name_entry2,text_1,label1
    sb = Scrollbar(window,orient= "vertical")
    sb2 = Scrollbar(window,orient= "horizontal")
    def vp():
        global mylist,sb
        dest()
        try :
            f = d.veiwcurrentpatients(sid)
            sb = Scrollbar(window,orient= "vertical")   
            mylist = Listbox(window, yscrollcommand = sb.set ,font = fonts(28))
            for i in f:
                mylist.insert(END,i)
            mylist.config(width=26)
            mylist.place(relx=o(900),rely=p(145))
            sb.config(command=mylist.yview)
            sb.place(relx=o(1335),rely=p(145),height = 167)
        except:x()
    def dp():
        global ching
        global pat_name_label,pat_name_entry,button_6,sb,sb2,mylist
        ching=''
        choice = StringVar()    
        dest()
        def submit():
            global ching
            global pat_name_label,pat_name_entry,button_6,sb,sb2,mylist
            try:
                ching=d.viewpatdoc(d.nametoid(choice.get()))
                sb = Scrollbar(window,orient= "vertical") 
                sb2 = Scrollbar(window,orient= "horizontal")  
                mylist = Listbox(window, yscrollcommand = sb.set , xscrollcommand= sb2.set,font = fonts(21),width=60)
                mylist.insert(END,'Name| Date of Admission| Ailment| Medication| Procedures')
                chong=[]
                for i in ching:
                    a=''
                    for j in i:
                        a+=(str(j)[:])
                        a+=(' |')
                    chong.append(a)
                for i in chong:
                    mylist.insert(END,i)
                mylist.place(relx=o(800),rely=p(240))
                sb.config(command=mylist.yview)
                sb.place(relx=o(780),rely=p(240),height = 255)
                sb2.config(command=mylist.xview)
                sb2.place(relx=o(780),rely=p(500),width=740) 
            except:x()            
        opt = d.veiwcurrentpatients(sid)
        pat_name_label = Label(window, text="CHOOSE PATIENT",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label.place(relx=o(900),rely=p(100))
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(900),rely=p(180))
        #pat_name_entry = OptionMenu(window,choice,*opt)
        #pat_name_entry.place(relx=o(900,rely=p(180)
        button_6 = Button(window,font= fonts(21),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(178.0),width=100.0,height=40.0)
    def ep():
        global ching
        global pat_name_label,pat_name_entry,button_6,sb,sb2,mylist,pat_name_entry2,pat_name_label2,text_1,label1,button_7
        ching=''
        choice = StringVar()
        select = StringVar()    
        dest()
        def submit():
            global pat_name_label,pat_name_entry,button_6,sb,sb2,mylist,pat_name_entry2,pat_name_label2,text_1,label1,button_7
            try:
               text_1.delete("1.0", "end-1c")
               text_1.insert(END,d.getinfo(select.get(),d.nametoid(choice.get()),sid))
            except:x()
        def submit2():
            d.setinfo(select.get(),d.nametoid(choice.get()),text_1.get("1.0", "end-1c"),sid)
            messagebox.showinfo('Success',"SUCCESS")
        opt = sorted(d.veiwcurrentpatients(sid))
        opt2 = ['Ailment','Medication','Procedures']
        pat_name_label = Label(window, text="CHOOSE PATIENT",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label.place(relx=o(900),rely=p(100))
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(900),rely=p(180))
        #pat_name_entry = OptionMenu(window,choice,*opt)
        #pat_name_entry.place(relx=o(900,rely=p(180)
        button_6 = Button(window,font= fonts(21),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(330.0),width=100.0,height=40.0)
        pat_name_label2 = Label(window, text="CHOOSE FIELD TO EDIT",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label2.place(relx=o(900),rely=p(270))
        pat_name_entry2 = OptionMenu(window,select,*opt2)
        pat_name_entry2.place(relx=o(900),rely=p(330))
        label1 =Label(window, text="ENTER UPDATED INFORMATION",font=fonts(30),bg = '#800020',fg='#150606')
        label1.place(relx=o(900),rely=p(400))
        text_1 = Text(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=fonts(21))
        text_1.place(relx=o(900.0),rely=p(450.0),width=400.0,height=150.0)
        button_7 = Button(window,font= fonts(21),text="APPLY EDIT",borderwidth=1,highlightthickness=0,command=submit2,relief="flat",fg = '#0E394C')
        button_7.place(relx=o(1272.0),rely=p(610.0),width=135.0,height=40.0)
    window.geometry("1536x888")
    window.configure(bg = "#FFFFFF")
    def paint():
        canvas = Canvas(window,bg = "#FFFFFF",height = 888,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(0.0,0.0,384.0,888.0,fill="#45CFB6",outline="")
        canvas.create_text(70.0,129.0,anchor="nw",text="WELCOME ",fill="#0E394C",font=fonts(51))
        canvas.create_text(10,230.0,anchor="nw",text=sname.split()[0].upper(),fill="#0E394C",font=fonts(36)) if ' ' in sname else canvas.create_text(10,230.0,anchor="nw",text=sname.upper(),fill="#0E394C",font=fonts(36))
        canvas.create_text(10,280.0,anchor="nw",text=sname.split()[1].upper(),fill="#0E394C",font=fonts(36)) if ' ' in sname else None
        canvas.create_rectangle(384.0,0.0,1536.0,888.0,fill="#800020",outline="")
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=vp,relief="flat").place(relx=o(416.0),rely=p(145.0),width=335.0,height=135.0)
        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=ep,relief="flat").place(relx=o(416.0),rely=p(603.0),width=335.0,height=139.0)
        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=dp,relief="flat").place(relx=o(416.0),rely=p(372.0),width=335.0,height=139.0)
        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=window.destroy,relief="flat").place(relx=o(1297.0),rely=p(799.0),width=227.0,height=69.0)
        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=lo,relief="flat").place(relx=o(1056.0),rely=p(799.0),width=227.0,height=69.0)
        window.attributes('-fullscreen', True)
        window.mainloop()
    paint()
if __name__ == '__main__':
    main(1)