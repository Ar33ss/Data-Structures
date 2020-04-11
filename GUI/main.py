import tkinter as tk
from LIsts import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.d_list()
        self.d_textbox()
        self.d_button()

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")
        #
        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")


    def d_list(self):
        listbox = tk.Listbox(self.master)
        listbox.pack(pady=40)

    def d_textbox(self):
        textbox = tk.Entry(self.master)
        textbox.pack(pady=40)

    def d_button(self):
        button = tk.Button(self.master, text="Insertar")
        button["command"] = self.say
        button.pack(pady=40)

    def say(self):
        print("Hello world")

root = tk.Tk()
root.geometry("800x800+50+50")
app = Application(master=root)
app.mainloop()