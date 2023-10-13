from pathlib import Path
import csv,os
from tkinter import Tk, Canvas, Entry,  Button, PhotoImage,messagebox,Label
import signuppage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{os.getcwd()}\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
fonts = lambda a:("Inter ExtraBold", a * -1,'bold')
x1=1536#x resolution
y1=888#y resolution
o = lambda a: a/x1
p= lambda a:a/y1
def login(nm,p,pro):
        with open("logindata.csv",'r') as f:
            for i in csv.reader(f):
                #   print(i)
                if i[0]==nm:
                        if i[3]==p:
                            if i[2] == pro:
                                messagebox.showinfo("Login", "Login Successful")
                                return(i[1])
                            else: return("PROFESSION")
                        else:
                            return("PASSWORD")     
            else:
                return('USERNAME')  
def main():
    def x(a):
        messagebox.showerror("ERROR", f"INCORRECT {a}, PLEASE RE-ENTER")
        window.destroy()
    def close(a=''):
        window.destroy()
        ching[3] = 'closed'
    window = Tk()
    ching=['','',True,'opened']
    def quartz():
        window.destroy()
        a = signuppage.main()
        ching[0]=a[0]
        ching[1] = a[1]
        ching[2] = False
        ching[3] = a[2]   
    def paint():
        window.configure(bg = "#FFFFFF")
        def submit(a=''):
            nm = name_var.get()
            pro = pro_var.get().lower()
            pwd = pass_var.get()
            ans = login(nm,pwd,pro)
            if ans == 'PASSWORD':x("PASSWORD")
            elif ans == "USERNAME":x('USERNAME')
            elif ans == "PROFESSION": x("PROFESSION")
            else:
                ching[0]=pro
                ching[1]=ans
                window.destroy()
        canvas = Canvas(window,bg = "#FFFFFF",height = 888,width = 1536,bd = 0,highlightthickness = 0,relief = "ridge")        
        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(file=relative_to_assets("docbackground.png"))
        Label(window,image=image_image_1).place(relx=o(0),rely=p(0))
        canvas.create_rectangle(933.0,0.0,1536.0,888.0,fill="#36A692",outline="")
        Label(window,text='LOGIN',fg='white',font=fonts(64),background='#36a692').place(relx=o(1106),rely=p(56))
        button_image_1 = PhotoImage(file=relative_to_assets("submitbuttonblue.png"))
        Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=submit,relief="flat").place(relx=o(1120.0),rely=p(668.0),width=241,height=83)
        button_image_2 = PhotoImage(file=relative_to_assets("closebuttonblue.png"))
        Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=close,relief="flat").place(relx=o(1347.0),rely=p(810.0),width=179,height=55)
        Label(window,text='Name',fg='white',font=fonts(48),background='#36a692').place(relx=o(953),rely=p(253))
        name_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '35')
        name_var.place(relx=o(1127.0),rely=p(245.0),width=382,height=59)
        Label(window,text='Profession',fg='white',font=fonts(48),background='#36a692').place(relx=o(953),rely=p(555))
        pro_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '35')
        pro_var.place(relx=o(1251.0),rely=p(555.0),width=254,height=55)
        Label(window,text='Password',fg='white',font=fonts(48),background='#36a692').place(relx=o(953),rely=p(395))
        pass_var = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font = '35',show = '*')
        pass_var.place(relx=o(1217.0),rely=p(392.0),width=287,height=55)
        button_image_3 = PhotoImage(file=relative_to_assets("singinbuttonblue.png"))
        Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=quartz,relief="flat").place(relx=o(1367),rely=p(55),width=163,height=79)
        window.attributes('-fullscreen', True)
        window.bind('<Return>',submit)
        window.bind('<Escape>',close)
        window.mainloop()
    paint()
    return(ching)
if __name__ == '__main__':
    main()
