import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        '''
        ## Add major portions of GUI
        self.statusbar = Statusbar(self, ...)
        self.toolbar = Toolbar(self, ...)
        self.navbar = Navbar(self, ...)
        self.main = Main(self, ...)
        '''

        ## <create the rest of your GUI here>

        # Create buttons
        self.button = tk.Button(self, text="QUIT", fg="red", command=self.quit)
        self.button.pack(side='left')

        self.hi_there = tk.Button(self, text="Hello", command=self.say_hi)
        self.hi_there.pack(side='right')

        # Creating a test variable to pass
        self.postit = "Test subject" 

    # Create a method to call
    def say_hi(self):
        self.hi_there.config(text="Bye there")
        print ("hi there, everyone!:", self.postit)

'''
## Create a class for each major portion of GUI
class Navbar(tk.Frame): ...
class Toolbar(tk.Frame): ...
class Statusbar(tk.Frame): ...
class Main(tk.Frame): ...
'''

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()