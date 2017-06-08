import tkinter as tk

LARGE_FONT = ("Verdana",14)
class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}
        frame=StartPage(container,self)
        self.frames[StartPage] = frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
def printName():
    print("hell")

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        theLabel = tk.Label(self, text="Start Page",font=LARGE_FONT)
        theLabel.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Let's Play!", fg="green", command=lambda:controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        theLabel = tk.Label(self, text="Page One", font=LARGE_FONT)
        theLabel.pack(pady=10, padx=10)
        button2 = tk.Button(self, text="Let's Play!", fg="green", command=lambda: controller.show_frame(StartPage))
        button2.pack()


app = Application()
app.mainloop()
