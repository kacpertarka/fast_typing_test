import threading
import tkinter as tk
import random
import time


class GUIApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.font = "Helvetica, 24"
        self.random_text = open("random.txt").read().split("\n")

        self.label = tk.Label(self.root, text=random.choice(self.random_text), font=self.font)
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        self.label.pack()

        self.input = tk.Entry(self.root, width=40, font=self.font)
        self.input.pack()
        self.input.bind("<KeyRelease>", self.start_time)

        self.show_label = tk.Label(self.root, text="Your time is\n 0CPS\n 0CPM", font=self.font)
        self.show_label.pack()

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.game = False
        self.counter = 0
        self.root.mainloop()

    def start_time(self, _):
        if not self.game:
            self.game = True
            threading.Thread(target=self.timer).start()
        if self.input.get() != self.label.cget("text"):
            self.input.config(fg="red")
        else:
            self.input.config(fg="black")
        if self.input.get() == self.label.cget("text"):
            self.game = False
            self.input.config(fg="green")

    def timer(self):
        while self.game:
            time.sleep(0.1)
            self.counter += 0.1
            characters_per_seconds = len(self.input.get()) / self.counter
            characters_per_minute = characters_per_seconds * 60
            self.show_label.config(text=f"""Your time is\n 
                                            {characters_per_seconds:.2f}CPS\n 
                                            {characters_per_minute:.2f}CPM""")

    def reset(self):
        self.counter = 0
        self.game = False
        self.label.config(text=random.choice(self.random_text))
        self.show_label.config(text="Your time is\n 0CPS\n 0CPM")
        self.input.delete(0, tk.END)
