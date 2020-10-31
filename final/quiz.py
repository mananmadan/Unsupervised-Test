# the json module to work with json files 
import json
import tkinter
from tkinter import *
import random
import sys
import time
from pynput import keyboard
time.sleep(10)
# questions = [
#     "How many Keywords are there in C Programming language ?",
#     "Which of the following functions takes A console Input in Python ?",
#     "Which of the following is the capital of India ?",
#     "Which of The Following is must to Execute a Python Code ?",
#     "The Taj Mahal is located in  ?",
#     "The append Method adds value to the list at the  ?",
#     "Which of the following is not a costal city of india ?",
#     "Which of The following is executed in browser(client side) ?",
#     "Which of the following keyword is used to create a function in Python ?",
#     "To Declare a Global variable in python we use the keyword ?",
# ]

# answers_choice = [
#     ["23","32","33","43",],
#     ["get()","input()","gets()","scan()",],
#     ["Mumbai","Delhi","Chennai","Lucknow",],
#     ["TURBO C","Py Interpreter","Notepad","IDE",],
#     ["Patna","Delhi","Benaras","Agra",],
#     ["custom location","end","center","beginning",],
#     ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
#     ["perl","css","python","java",],
#     ["function","void","fun","def",],
#     ["all","var","let","global",],
# ] 
## helper function for keyboard listener
def on_press(key):
        if key.char == 'q':
            print("killing")
            sys.exit()

## helper function for keyboard listener
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def wait_key():
 with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

# load questions and answer choices from json file instead of the file
with open('data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice 
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,1,1,1,3,1,0,1,3,3] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelresulttext.configure(text="Score : " + str(score) + "\n Keep It Up !!")
        labelimage.image = img
        #labelresulttext.configure(text="You Are Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelresulttext.configure(text="Score : "+ str(score) + "\n You Can Be Better !!")
        labelimage.image = img
        #labelresulttext.configure(text="")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelresulttext.configure(text="Score : "+ str(score) + "\n You Should Work Hard")
        labelimage.image = img
        #labelresulttext.configure(text=" !!")
def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)

ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
        print("finally here")
        #root.destroy()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Quiz")
w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)
img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quiz",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,70))

lblRules = Label(
    root,
    text = " Rules : \n All questions are compulsary \n No Negetive Marking \n This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
