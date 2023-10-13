from pathlib import Path
import os
from dbms import addstaff,nametoid
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox,Label
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{os.getcwd()}\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
fonts = lambda a:("Inter ExtraBold", a * -1,'bold')
x1=1536#x resolution
y1=888#y resolution
o = lambda a: a/x1
p= lambda a:a/y1
def x():
    messagebox.showerror("ERROR", "INVALID INPUT, PLEASE RE-ENTER")
def main():
    ching=['','','opened'] 
    pane = Tk()
    def paint():
        pane.configure(bg = "#FFFFFF")
        def submit():
            nm = name_var.get()
            pro = pro_var.get().lower()
            pwd = pass_var.get()
            if nm and pro and pwd != '':
                idd=addstaff(nm,pro,pwd)
                ching[0]=(pro)
                ching[1] = idd
                pane.destroy()
            else:
                x()
                ching.append('opened')
                pane.destroy()
        canvas = Canvas(pane,bg = "#FFFFFF",height = 888,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(file=relative_to_assets("docbackground.png"))
        Label(pane,image=image_image_1).place(relx=o(0),rely=p(0))
        canvas.create_rectangle(933.0,0.0,1536.0,888.0,fill="#36A692",outline="")
        Label(pane,text='SIGN UP',fg='white',font=fonts(64),background='#36a692').place(relx=o(1104),rely=p(78))
        button_image_1 = PhotoImage(file=relative_to_assets("submitbuttonblue.png"))
        Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=submit,relief="flat").place(relx=o(1120),rely=p(668.0),width=241,height=83.28125)
        button_image_2 = PhotoImage(file=relative_to_assets("closebuttonblue.png"))
        Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=pane.destroy,relief="flat").place(relx=o(1347.0),rely=p(810.0),width=179,height=58.28125)
        Label(pane,text='Name',fg='white',font=fonts(48),background='#36a692').place(relx=o(953),rely=p(253))
        name_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '26')
        name_var.place(relx=o(1127.0),rely=p(245.0),width=382,height=59)
        Label(pane,text='Profession',fg='white',font=fonts(48),background='#36a692').place(relx=o(953),rely=p(555))
        pro_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '26')
        pro_var.place(relx=o(1251.0),rely=p(555.0),width=254,height=55)
        Label(pane,text='Password',fg='white',font=fonts(48),background='#36a692').place(relx=o(953),rely=p(400))
        pass_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '26',show = '*')
        pass_var.place(relx=o(1217.0),rely=p(392.0),width=287,height=55)
        pane.attributes('-fullscreen', True)
        pane.bind('<Escape>',lambda a:pane.destroy())
        pane.bind('<Return>',lambda a:pane.destroy())
        pane.mainloop()
    paint()
    return(ching[0],ching[1],ching[2])

if __name__ == '__main__':
    main()