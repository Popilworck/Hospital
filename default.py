from pathlib import Path
import os
from dbms import addstaff,nametoid
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{os.getcwd()}\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
fonts = lambda a:("Inter ExtraBold", a * -1,'bold')

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
        image_1 = canvas.create_image(469.0,444.0,image=image_image_1)
        canvas.create_rectangle(933.0,0.0,1536.0,888.0,fill="#36A692",outline="")
        canvas.create_text(1104.0,78.0,anchor="nw",text="SIGN UP",fill="#FFFFFF",font=fonts(64))
        button_image_1 = PhotoImage(file=relative_to_assets("submitbuttonblue.png"))
        button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=submit,relief="flat")
        button_1.place(x=1120.0,y=668.0,width=241,height=83.28125)
        button_image_2 = PhotoImage(file=relative_to_assets("closebuttonblue.png"))
        button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=pane.destroy,relief="flat")
        button_2.place(x=1347.0,y=810.0,width=179,height=58.28125)
        canvas.create_text(952.0,253.0,anchor="nw",text="Name",fill="#FFFFFF",font=fonts(48))
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(1318,275,image=entry_image_1)
        name_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '26')
        name_var.place(x=1127.0,y=245.0,width=382,height=59)  
        canvas.create_text(948.0,555.0,anchor="nw",text="Profession",fill="#FFFFFF",font=fonts(48))
        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(1378,583,image=entry_image_2)
        pro_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '26')
        pro_var.place(x=1251.0,y=555.0,width=254,height=55)
        canvas.create_text(943.0,400.0,anchor="nw",text="Password",fill="#FFFFFF",font=fonts(48))
        entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(1360,420,image=entry_image_4)
        pass_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '26',show = '*')
        pass_var.place(x=1217.0,y=392.0,width=287,height=55)
        pane.attributes('-fullscreen', True)
        pane.bind('<Escape>',lambda a:pane.destroy())
        pane.bind('<Return>',lambda a:pane.destroy())
        pane.mainloop()
    paint()
    return(ching[0],ching[1],ching[2])

if __name__ == '__main__':
    main()