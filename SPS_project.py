from tkinter import *
from PIL import Image,ImageTk
from playsound import playsound
from random import * 


root = Tk()
root.title('Rock Paper Scissor')
root.iconbitmap('rps.ico')
root.geometry("1100x500")
root.configure(background='black')


root.resizable(width=False, height=False)
root.wm_attributes("-topmost", 0)

'''--------------------------------------------------LABEL------------------------------------------------------'''

l1 = Label(root,text="STONE PAPER SCISSOR",fg='#5cffec',bg='black',font="Tinmes 35 bold ")
l1.grid(row=0,column=2)

b1 = Button(root, text="EXIT",font="Arial 15 bold",bg='#f21b1b',fg='white',command=root.destroy)
b1.grid(row=0,column = 3)

l2 = Label(root,text = "COMPUTER",font ="Times 25 bold",bg='black',fg='#ebd3e4').grid(row = 2,column = 1,pady=20)

l3 = Label(root,text = "PLAYER",font ="Times 25 bold",bg='black',fg='#ebd3e4').grid(row = 2,column = 2,pady=20)

l3 = Label(root,text = "RESULT",font ="Times 25 bold",bg='black',fg='#ebd3e4').grid(row = 2,column = 3,pady=20)

'''--------------------------------------------------IMAGES------------------------------------------------------'''

rHandPhoto = PhotoImage(file = 'rHand.png')
pHandPhoto = PhotoImage(file = 'pHand.png')
sHandPhoto = PhotoImage(file = 'sHand.png')

rockPhoto = PhotoImage(file = 'rock.png')
paperPhoto = PhotoImage(file = 'paper.png')
scissorsPhoto = PhotoImage(file = 'scissors.png')

winPhoto = PhotoImage(file = 'win.png')
loosePhoto = PhotoImage(file = 'loose.png')
tiePhoto = PhotoImage(file = 'tie.png')

'''-----------------------------------------------COMP PLAYER LABEL------------------------------------------------'''

comp_label = Label(root,image=rockPhoto,bg='black',pady=40)
user_label = Label(root,image=paperPhoto,bg='black',pady=40)
WinLose_label = Label(root,image=scissorsPhoto,bg='black',pady=40)

comp_label.grid(row=10,column=1)
user_label.grid(row=10,column=2)
WinLose_label.grid(row=10,column=3)

'''--------------------------------------------------FUNCTION------------------------------------------------------'''

choices = ["rock","paper","scissor"]

def choice(yourChoice):
    
    compChoice = choices[randint(0,2)]

    if yourChoice == "rock":
        user_label.configure(image = rHandPhoto)
        if compChoice == "rock":
           comp_label.configure(image = rHandPhoto)
           WinLose_label.configure(image = tiePhoto)
           
        elif compChoice == "paper":
             comp_label.configure(image = pHandPhoto)
             WinLose_label.configure(image = loosePhoto)
        else:
            comp_label.configure(image = sHandPhoto)    
            WinLose_label.configure(image = winPhoto)
            
    elif yourChoice == "paper":
        user_label.configure(image = pHandPhoto)  
        if compChoice =="rock":
             comp_label.configure(image = rHandPhoto)
             WinLose_label.configure(image = winPhoto)
        elif compChoice == "paper":
             comp_label.configure(image = pHandPhoto)
             WinLose_label.configure(image = tiePhoto)
        else:
             comp_label.configure(image = sHandPhoto)
             WinLose_label.configure(image = loosePhoto)
                 
    elif yourChoice == "scissor":
        user_label.configure(image = sHandPhoto)  
        if compChoice =="rock":
            comp_label.configure(image = rHandPhoto)
            WinLose_label.configure(image = loosePhoto)
        elif compChoice =="paper":
            comp_label.configure(image = pHandPhoto)
            WinLose_label.configure(image = winPhoto)
        else:
            comp_label.configure(image = sHandPhoto)
            WinLose_label.configure(image = tiePhoto)
    else:
        if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
            user_label.configure(image = rHandPhoto)
            user_label.configure(image = pHandPhoto)
            user_label.configure(image = sHandPhoto)
        


'''--------------------------------------------------BUTTONS------------------------------------------------------'''

rock = Button(root,text ="ROCK",width=20,height = 2,font = "Arial 10 bold",bg='#c0d9bd',border='2',
command=lambda:choice('rock')).grid(row=55,column=1,pady =30,padx=20)

paper = Button(root,text ="PAPER",width=20,height = 2,font = "Arial 10 bold",bg='#c0d9bd',
command=lambda:choice('paper')).grid(row=55,column= 2,pady =30)

scissor = Button(root,text ="SCISSOR",width=20,height = 2,font = "Arial 10 bold",bg='#c0d9bd',
command=lambda:choice('scissor')).grid(row=55,column=3,pady=30)
    
root.mainloop()