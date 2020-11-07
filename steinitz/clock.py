from tkinter import Frame, PhotoImage, Label, E, W, BOTH, Tk
from steinitz.stopwatch import Stopwatch
from steinitz.utils import rsc

class Clock(Frame):
    def __init__(self, root, **kwargs):
        Frame.__init__(self, master=root, board=None, game=None, **kwargs)

        self.root   = root
        self.img1   = PhotoImage(file=rsc('icon', 'bp.gif'))
        self.img2   = PhotoImage(file=rsc('icon', 'wp.gif'))
        self.main   = Frame(self)
        self.label1 = Label(master=self.main, anchor=E, text='Black', image=self.img1)
        self.label2 = Label(master=self.main, anchor=E, text='White', image=self.img2)
        self.label3 = Stopwatch(master=self.main, anchor=W, font=('Helvetica', 12))
        self.label4 = Stopwatch(master= self.main, anchor=W, font=('Helvetica', 12))

        self.main.pack(side='top', expand=True, fill=BOTH)
        self.label1.pack(side='left', expand=True, fill=BOTH)
        self.label3.pack(side='left', expand=True, fill=BOTH)
        self.label2.pack(side='left', expand=True, fill=BOTH)
        self.label4.pack(side='left', expand=True, fill=BOTH)


    def click(self, turn, white, black):
        self.label3.sched(black)
        self.label4.sched(white)

        if turn == 'B': self.black_turn()
        else: self.white_turn()
    
    def black_turn(self):
        self.label4.stop()
        self.label3.start()

    def white_turn(self):
        self.label3.stop()
        self.label4.start()


if __name__ == '__main__':
    app = Tk()
    alpha = Clock(app)
    alpha.pack()
    alpha.click_black(500)
    alpha.click_white(400)
    app.mainloop()



