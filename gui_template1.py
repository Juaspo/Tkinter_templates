# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class MainApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # dict of pages

        for F in (StartPage, PageOne): # Add pages to dict here
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(F)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

## For creating a new page copy this class and modify
class StartPage(tk.Frame): # Page example 1
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello World", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        btn = tk.Button(self, text="Go2", command=lambda: controller.show_frame(PageOne))
        btn.pack()

class PageOne(tk.Frame): # Page example 2
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello Earth", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        btn = tk.Button(self, text="Go1", command=lambda: controller.show_frame(StartPage))
        btn.pack()

app = MainApplication()
app.mainloop()
