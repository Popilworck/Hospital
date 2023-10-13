from pathlib import Path
import os,dbms as d
from tkinter import messagebox
import main_,signuppage
from tkinter import *
from tkinter import ttk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{os.getcwd()}\adminmenu\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
fonts = lambda a:("Inter ExtraBold", a * -1,'bold')
x1=1536#x resolution
y1=888#y resolution
o = lambda a: a/x1
p= lambda a:a/y1
def dest(l=['mylist','sb','pat_name_label','pat_name_entry','button_6','label1','label2','label3','entry_1','entry_2','entry_3','sb2','mylist']):
        for i in l:
            try:
                exec(f'{i}.destroy()')
            except:pass
def x():
    messagebox.showerror("ERROR", "INVALID INPUT, PLEASE RE-ENTER")
def patmain(sid): 
    def staffmainstart():
        window.destroy()
        staffmain(sid)
    window = Tk()
    window.bind('<Escape>',lambda a:window.destroy())
    canvas = Canvas(window,bg = "#FFFFFF",height = 888,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
    global mylist,sb,pat_name_entry,pat_name_label,button_6,sb2,entry_1,label1,label2,label3,entry_1,entry_2,entry_3
    sb = Scrollbar(window,orient= "vertical")
    sb2 = Scrollbar(window,orient= "horizontal")    
    def vpd():
        global ching
        global pat_name_label,pat_name_entry,button_6,mylist,sb
        ching=''
        choice = StringVar()    
        dest()
        def submit():
            global pat_name_label,pat_name_entry,button_6,mylist,sb
            dest(['mylist','sb'])
            try:
                ching=d.veiwcurrentpatients(d.nametoidd(choice.get()))
                sb = Scrollbar(window,orient= "vertical") 
                mylist = Listbox(window, yscrollcommand = sb.set ,font = fonts(21),width=40)
                mylist.insert(END,'Name')
                for i in ching:
                    mylist.insert(END,i)
                mylist.place(relx=o(900),rely=p(240))
                sb.config(command=mylist.yview)
                sb.place(relx=o(880),rely=p(240),height = 255)
            except:x()    
        opt = sorted(d.showdoc())
        pat_name_label = Label(window, text="CHOOSE DOCTOR",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label.place(relx=o(900),rely=p(100))
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(900),rely=p(180))
        button_6 = Button(window,font= fonts(21),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(178.0),width=100.0,height=40.0)
    def ap():
        global ching
        global pat_name_label,pat_name_entry,button_6,label3,label2,label1,entry_1,entry_2,entry_3
        ching=''
        choice = StringVar()    
        dest()
        def submit():
            try:
                #print(d.nametoidd(choice.get()))
                d.addpatient(e1.get(),e3.get(),e2.get,d.nametoidd(choice.get()))
                messagebox.showinfo("Success","SUCCESSFULLY ADDED PATIENT")
            except:x()            
        opt = sorted(d.showdoc())
        e1,e2,e3='','',''
        pat_name_label = Label(window, text="CHOOSE DOCTOR",font=fonts(36),bg = '#800020',fg='#390404')
        pat_name_label.place(relx=o(793),rely=p(100))
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(793),rely=p(170))
        #pat_name_entry = OptionMenu(window,choice,*opt)
        #pat_name_entry.place(relx=o(793,rely=p(170)
        button_6 = Button(window,font= fonts(20),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(178.0),width=100.0,height=40.0)
        label1 = Label(window,fg="#390404",font=fonts(36) ,text ="Enter Patient Name",bg = '#800020')
        label1.place(relx=o(793),rely=p(220))
        entry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=fonts(24),textvariable=e1)
        entry_1.place(relx=o(800),rely=p(270),width=300.0,height=40.0)
        label2 = Label(window,fg="#390404",font=fonts(36) ,text ="Enter Patient Phone Number",bg = '#800020',textvariable=e2)
        label2.place(relx=o(793),rely=p(320))
        entry_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=fonts(24))
        entry_2.place(relx=o(800),rely=p(370),width=300.0,height=40.0)
        label3 = Label(window,fg="#390404",font=fonts(36) ,text ="Enter Patient Address",bg = '#800020',textvariable=e3)
        label3.place(relx=o(793),rely=p(420))
        entry_3 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=fonts(24))
        entry_3.place(relx=o(800),rely=p(470),width=300.0,height=40.0)
    def lo():
        window.destroy()
        main_.start()
    def vp():
        global mylist,sb,pat_name_entry,pat_name_label,button_6,sb2,entry_1,label1
        dest()
        try:
            v=[]
            for i in d.showallcurrentpatients():
                v.append((i[1],i[0]))
            sb = Scrollbar(window,orient= "vertical")   
            mylist = Listbox(window, yscrollcommand = sb.set ,font = fonts(28),width=26)
            for i in sorted(v):
                k = f'{i[1]} - {i[0][:]}'
                mylist.insert(END,k)
            mylist.place(relx=o(900),rely=p(145))
            sb.config(command=mylist.yview)
            sb.place(relx=o(1335),rely=p(145),height = 344)
        except:
            x()
    def rp():
        global pat_name_label,pat_name_entry,button_6,mylist,sb
        choice = StringVar()    
        dest()
        def submit():
            global pat_name_label,pat_name_entry,button_6
            try:
                d.removepatient(d.nametoid(p=choice.get()))
                messagebox.showinfo("Success","Patient Succesfully removed")
            except:x()
        opt=[]
        for i in d.showallcurrentpatients():
            opt.append(i[1])
        opt.sort()
        pat_name_label = Label(window, text="CHOOSE PATIENT TO REMOVE",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label.place(relx=o(900),rely=p(100))
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(900),rely=p(180))
        #pat_name_entry = OptionMenu(window,choice,*opt)
        #pat_name_entry.place(relx=o(900),rely=p(180)
        button_6 = Button(window,font= fonts(20),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(178.0),width=100.0,height=40.0)
    def vp1():
        global ching
        global pat_name_label,pat_name_entry,button_6,sb,sb2,mylist
        ching=''
        choice = StringVar()    
        dest()
        def submit():
            global ching
            global pat_name_label,pat_name_entry,button_6,sb,sb2,mylist
            dest(['mylist','sb','sb2'])
            try:
                ching=d.viewpat(d.nametoid(choice.get()))
                sb = Scrollbar(window,orient= "vertical") 
                sb2 = Scrollbar(window,orient= "horizontal")  
                mylist = Listbox(window, yscrollcommand = sb.set , xscrollcommand= sb2.set,font = fonts(21),width=60)
                mylist.insert(END,'Admission Id| Staff Id|Patient Id| Name| Date of Admission| Date of Release|Ailment| Medication| Procedures| Address')
                chong=[]
                #print(ching)
                for i in ching:
                    a = ''
                    for j in range(len(i)):
                        if j == 2:
                            a+=(str(i[j])[:])
                            a+=(' |')
                            a+=(d.idtoname(p=i[j]))
                            a+=' |'
                        elif i[j] == None:
                            a+='- |'
                        else:
                            a+=(str(i[j])[:])
                            a+=(' |')   
                    chong.append(a)
                for i in chong:
                    mylist.insert(END,i)
                mylist.place(relx=o(800),rely=p(240))
                sb.config(command=mylist.yview)
                sb.place(relx=o(780),rely=p(240),height = 255)
                sb2.config(command=mylist.xview)
                sb2.place(relx=o(780),rely=p(500),width=740) 
            except :x()
        opt=[]        
        for i in (d.showallcurrentpatients()):
            opt.append(i[1])
        opt.sort()
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(900),rely=p(180))
        pat_name_label = Label(window, text="CHOOSE PATIENT",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label.place(relx=o(900),rely=p(100))
       # pat_name_entry = OptionMenu(window,choice,*opt)
       # pat_name_entry.place(relx=o(900),rely=p(180)
        button_6 = Button(window,font= fonts(20),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(178.0),width=100.0,height=40.0)
        #add doctor remove doctor  update doctor info
    window.geometry("1536x888")
    window.configure(bg = "#FFFFFF")
    canvas = Canvas(window,bg = "#FFFFFF",height = 888,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(384.0,1.1368683772161603e-13,1536.0,888,fill="#800020",outline="")
    canvas.create_rectangle(0.0,1.1368683772161603e-13,384.0,888,fill="#45CFB7",outline="")
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=vpd,relief="flat").place(relx=o(399.0),rely=p(61),width=328.0,height=124.0)
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    Button(image=button_image_2,borderwidth=0,highlightthickness=0,relief="flat",command=staffmainstart).place(relx=o(24.0),rely=p(500),width=335.0,height=135.0)
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    Button(image=button_image_3,borderwidth=0,highlightthickness=0,relief="flat",command = dest).place(relx=o(24.0),rely=p(304.9),width=335.0,height=135.0)
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=ap,relief="flat").place(relx=o(399.0),rely=p(200),width=328.0,height=128.0)
    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=vp,relief="flat").place(relx=o(399.0),rely=p(350),width=328.0,height=128.0)
    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=vp1,relief="flat").place(relx=o(399.0),rely=p(500),width=328.0,height=128.0)
    button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
    Button(image=button_image_9,borderwidth=0,highlightthickness=0,command=rp,relief="flat").place(relx=o(401.0),rely=p(650),width=326.0,height=126.0)
    button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
    Button(image=button_image_10,borderwidth=0,highlightthickness=0,command=window.destroy,relief="flat").place(relx=o(1297.0),rely=p(798.9),width=227.0,height=69.0)
    button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
    Button(image=button_image_11,borderwidth=0,highlightthickness=0,command=lo,relief="flat").place(relx=o(1056.0),rely=p(798.9),width=227.0,height=69.0)
    canvas.create_text(70.0,52,anchor="nw",text="WELCOME ",fill="#0E394C",font=fonts(43))
    canvas.create_text(60.0,113,anchor="nw",text=(d.idtoname(s=sid).split()[0]),fill="#0E394C",font=fonts(43))
    try:canvas.create_text(60.0,160,anchor="nw",text=(d.idtoname(s=sid).split()[1]),fill="#0E394C",font=fonts(43))
    except:pass
    window.attributes('-fullscreen',True)
    window.mainloop()
def staffmain(sid):
    def patmainstart():
        window.destroy()
        patmain(sid)
    def lo():
        window.destroy()
        main_.start()
    window = Tk()
    window.bind('<Escape>',lambda a:window.destroy())
    window.geometry("1536x888")
    window.configure(bg = "#FFFFFF")
    canvas = Canvas(window,bg = "#FFFFFF",height = 888,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    def ep():
        global ching
        global pat_name_label,pat_name_entry,button_6,pat_name_entry2,pat_name_label2,text_1,label1,button7
        ching=''
        choice = StringVar()
        select = StringVar()    
        dest()
        def submit():
            global pat_name_label,pat_name_entry,button_6,pat_name_entry2,pat_name_label2,text_1,label1,button7
            try:
               text_1.delete("1.0", "end-1c")
               text_1.insert(END,d.getinfos(select.get(),d.nametoidd(choice.get())))
            except:x()
        def submit2():
            d.setinfos(select.get(),text_1.get("1.0", "end-1c"),d.nametoidd(choice.get()))
            messagebox.showinfo('Success',"SUCCESS")
        opt = []
        for i in d.showstaff():
            opt.append(i[0])
        opt.sort()
        opt2 = ['Name','Designation']
        pat_name_label = Label(window, text="CHOOSE STAFF MEMBER",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label.place(relx=o(900),rely=p(100))
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(900),rely=p(180))
        #pat_name_entry = OptionMenu(window,choice,*opt)
        #pat_name_entry.place(relx=o(900),rely=p(180)
        button_6 = Button(window,font= fonts(20),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(330.0,width=100.0,height=40.0))
        pat_name_label2 = Label(window, text="CHOOSE FIELD TO EDIT",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label2.place(relx=o(900),rely=p(270))
        pat_name_entry2 = ttk.Combobox(window, textvariable=select, values=opt2)
        pat_name_entry2.place(relx=o(900),rely=p(330))
        #pat_name_entry2 = OptionMenu(window,select,*opt2)
        #pat_name_entry2.place(relx=o(900),rely=p(330)
        label1 =Label(window, text="ENTER UPDATED INFORMATION",font=fonts(30),bg = '#800020',fg='#150606')
        label1.place(relx=o(900),rely=p(400))
        text_1 = Text(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=fonts(21))
        text_1.place(relx=o(900.0),rely=p(450.0),width=400.0,height=150.0)
        button7 = Button(window,font= fonts(20),text="APPLY EDIT",borderwidth=1,highlightthickness=0,command=submit2,relief="flat",fg = '#0E394C')
        button7.place(relx=o(1272.0),rely=p(610.0,width=135.0,height=40.0))
    def rp():
        global pat_name_label,pat_name_entry,button_6,mylist,sb
        choice = StringVar()    
        dest()
        def submit():
            global pat_name_label,pat_name_entry,button_6
            try:
                d.remstaff(d.nametoidd(choice.get()))
            except:x()       
        opt=[]
        for i in d.showstaff():
            opt.append(i[0])
        opt.sort()
        pat_name_label = Label(window, text="CHOOSE STAFF MEMBER",font=fonts(36),bg = '#800020',fg='#150606')
        pat_name_label.place(relx=o(900),rely=p(100))
        pat_name_entry = ttk.Combobox(window, textvariable=choice, values=opt)
        pat_name_entry.place(relx=o(900),rely=p(180))
        #pat_name_entry = OptionMenu(window,choice,*opt)
        #pat_name_entry.place(relx=o(900),rely=p(180)
        button_6 = Button(window,font= fonts(20),text="SUBMIT",borderwidth=1,highlightthickness=0,command=submit,relief="flat",fg = '#0E394C')
        button_6.place(relx=o(1272.0),rely=p(178.0),width=100.0,height=40.0)
    def vp():
        global mylist,sb,pat_name_entry,pat_name_label,button_6,sb2,entry_1,label1
        dest()
        try :
            f = [i[0] for i in d.showstaff()]
            sb = Scrollbar(window,orient= "vertical")   
            mylist = Listbox(window, yscrollcommand = sb.set ,font = fonts(28),width=20)
            for i in sorted(f):
                mylist.insert(END,i)
            mylist.place(relx=o(900),rely=p(145))
            sb.config(command=mylist.yview)
            sb.place(relx=o(1000+220),rely=p(145),height = 344)
        except:
            x()
    def ap():
        window.destroy()
        signuppage.main()
        patmain(sid)
    canvas.create_rectangle(384.0,1.1368683772161603e-13,1536.0,888,fill="#800020",outline="")
    canvas.create_rectangle(0.0,1.1368683772161603e-13,384.0,888,fill="#45CFB7",outline="")
    button_image_1 = PhotoImage(file=relative_to_assets("button_12.png"))
    Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=ap,relief="flat").place(relx=o(397.0),rely=p(101.9),width=328.0,height=124.0)
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=dest,relief="flat").place(relx=o(24.0),rely=p(488.9),width=335.0,height=135.0)
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=patmainstart,relief="flat").place(relx=o(24.0),rely=p(304.9),width=335.0,height=135.0)
    button_image_5 = PhotoImage(file=relative_to_assets("button_14.png"))
    Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=ep,relief="flat").place(relx=o(399.0),rely=p(281.9),width=328.0,height=128.0)
    button_image_6 = PhotoImage(file=relative_to_assets("button_13.png"))
    Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=rp,relief="flat").place(relx=o(399.0),rely=p(465.9),width=328.0,height=128.0)
    button_image_7 = PhotoImage(file=relative_to_assets("button_15.png"))
    Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=vp,relief="flat").place(relx=o(397.0),rely=p(650.9),width=328.0,height=128.0)
    button_image_8 = PhotoImage(file=relative_to_assets("button_10.png"))
    Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=window.destroy,relief="flat").place(relx=o(1297.0),rely=p(798.9),width=227.0,height=69.0)
    button_image_9 = PhotoImage(file=relative_to_assets("button_11.png"))
    Button(image=button_image_9,borderwidth=0,highlightthickness=0,command=lo,relief="flat").place(relx=o(1056.0),rely=p(798.9),width=227.0,height=69.0)
    canvas.create_text(70.0,52.999999999999886,anchor="nw",text="WELCOME ",fill="#0E394C",font=fonts(43))
    canvas.create_text(60.0,113,anchor="nw",text=(d.idtoname(s=sid).split()[0]),fill="#0E394C",font=fonts(43))
    canvas.create_text(60.0,160,anchor="nw",text=(d.idtoname(s=sid).split()[1]),fill="#0E394C",font=fonts(43))
    window.attributes('-fullscreen',True)
    window.mainloop()
if __name__ == '__main__':
    patmain(0)