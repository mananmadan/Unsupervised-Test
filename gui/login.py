from tkinter import *
from PIL import Image, ImageTk
import sys
#--------------------------------------------------------------------------------------------------------------
#create the window and add size and title to it
window = Tk()
window.geometry("800x500+300+100")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("Login Page")

def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string)
#---------------------------------------------------------------------------------------------------------------
#first get the picture then save it in pic and set as background
image = Image.open("blueBG.jpg")
pic = ImageTk.PhotoImage(image)

label0 = Label(image = pic)
label0.pack(fill = BOTH, expand = 'yes')

#------------------------------------------------------------
# -------------------------------------------------
#functions for the buttons to perform
def login():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    username = userName.get()
    Pass = password.get()
    username=remove(username)
    if username in users :
        if (users[username] == Pass):
            label4 = Label(window, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)
            sys.exit()
            
        else:
            label4 = Label(window, text = ("Incorrect Password for " + username),width = 25, font = ("arial", 30, "bold"))
            label4.place(x = 0, y = 400)

    else:
        label4 = Label(window, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
        label4.place(x = 0, y = 400)

#----------------------------------------------------------------------------------------------------------------
#first lable
label1 = Label(window, text = " Login System ", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 200, y = 15)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"),show='*')
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 335, y = 340)

#display window
window.mainloop()
