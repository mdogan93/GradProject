from tkinter import *
import tkinter.messagebox

class BuckysButtons:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton =  Button(frame,text="Print Message",fg="green",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton =  Button(frame,text="Quit",fg="green",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("This is Bucky's message")
root = Tk()

# b= BuckysButtons(root)
#
# def printName():
#     print("hell")
#
# def printDontLeave(event):
#     print("Dont leave me alone")
#
# tkinter.messagebox.showinfo("Helll","No where to go")
# theLabel = Label(root,text="Test your architecture knowledge")
# theLabel.pack()
#
# topFrame = Frame(root)
# topFrame.pack()
#
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame,text="Let's Play!",fg="green",command=printName)
# button2 = Button(bottomFrame,text="Leave The Game!",fg="red")
# button2.bind("<Button-1>",printDontLeave)
# button1.pack()
# button2.pack(side=RIGHT)
#
# lblOne = Label(root,text="Label One",bg="red",fg="white")
# lblOne.pack()
# lblTwo = Label(root,text="Label Two",bg="green",fg="white")
# lblTwo.pack(fill=X)
# lblTwo = Label(root,text="Label Three",bg="blue",fg="white")
# lblTwo.pack(side=LEFT,fill=Y)

root.mainloop()