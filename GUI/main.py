import tkinter as tk
from LIsts import *

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.l = None

    def create_widgets(self):
        listbox = tk.Listbox(self.master)
        listbox.pack(pady=40)

        textbox = tk.Entry(self.master)
        textbox.pack(pady=40)

        button = tk.Button(self.master, text="Insertar", command = lambda: self.printv(textbox.get(), listbox))
        button.pack(pady=40)



        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        #
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")


    def d_list(self):
        pass

    def d_textbox(self):
        pass

    def d_button(self):
        pass

    def printv(self, string, listbox):
        listbox.insert(tk.END, string)



root = tk.Tk()
root.geometry("800x800+50+50")
app = Application(master=root)
app.mainloop()