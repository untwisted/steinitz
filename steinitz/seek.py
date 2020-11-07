from tkinter import Frame, PhotoImage, Label, E, BOTH, Toplevel, RAISED, StringVar, Radiobutton, X, Entry, END, Checkbutton, Button
from steinitz.utils import rsc

class Seek(Toplevel):
    def __init__(self, root):
        Toplevel.__init__(self, master=root)

        self.root = root

        self.title('Match')

        self.resizable(height=False, width=False)
        self.transient(self.root)

        self.frame1 = Frame(master=self, padx=5, pady=5, border=3, relief=RAISED)

        self.img1 = PhotoImage(master=self.frame1, file=rsc('icon', 'wp.gif'))
        self.img2 = PhotoImage(master=self.frame1, file=rsc('icon', 'bp.gif'))

        self.color = StringVar()

        self.color.set('white') 

        self.rated = StringVar()

        self.rated.set('rated')

        self.radiobutton1 = Radiobutton(master=self.frame1, image=self.img1, indicatoron=0,variable=self.color,value='white')
        self.radiobutton2 = Radiobutton(master=self.frame1, image=self.img2, indicatoron=0,variable=self.color,value='black')

        self.radiobutton1.pack(side='left', expand=True, fill=X)
        self.radiobutton2.pack(side='left', expand=True, fill=X)

        self.frame1.pack(side='top', fill=BOTH)

        self.frame2 = Frame(master=self, padx=5, pady=5, border=3,relief=RAISED)
        self.label1 = Label(master=self.frame2, text='Time:')
        self.entry1 = Entry(master=self.frame2)
        self.entry1.insert(END, '15')

        self.label2 = Label(master=self.frame2, text='Increment:')
        self.entry2 = Entry(master=self.frame2)
        self.entry2.insert(END, '0')

        self.label3 = Label(master=self.frame2, text='Min rating:')
        self.entry3 = Entry(master=self.frame2)
        self.entry3.insert(END, '1600')

        self.label4 = Label(master=self.frame2, text='Max rating:')
        self.entry4 = Entry(master=self.frame2)
        self.entry4.insert(END, '1700')

        self.label1.grid(row=0, column=0, sticky=E)
        self.entry1.grid(row=0, column=1, sticky=E)
        self.label2.grid(row=1, column=0, sticky=E)
        self.entry2.grid(row=1, column=1, sticky=E)

        self.label3.grid(row=2, column=0, sticky=E)
        self.entry3.grid(row=2, column=1, sticky=E)

        self.label4.grid(row=3, column=0, sticky=E)
        self.entry4.grid(row=3, column=1, sticky=E)


        self.frame2.pack(side='top', fill=BOTH)

        self.frame3       = Frame(master=self, padx=5, pady=5, border=3, relief=RAISED)
        self.checkbutton1 = Checkbutton(master=self.frame3, text='Rated', indicatoron=0, 
                                        variable=self.rated, onvalue='rated', offvalue='unrated')

        self.checkbutton1.pack(side='left', expand=True, fill=X)
        self.frame3.pack(side='top', fill=BOTH)
           

        self.frame4  = Frame(master=self,padx=5, pady=5, border=3, relief=RAISED)
        self.button1 = Button(master=self.frame4,text='Ok', command=self.ok)
        self.button2 = Button(master=self.frame4,text='Cancel', command=self.cancel)
        self.button1.pack(side='left', expand=True, fill=BOTH)
        self.button2.pack(side='left', expand=True, fill=BOTH)

        self.frame4.pack(side='top', fill=BOTH)
        self.root.board.wait_window(self)
        # self.grab_set()


    def ok(self):
        self.info = (self.entry1.get(), self.entry2.get(), str(self.rated.get()), 
                     self.color.get(), self.entry3.get(), self.entry4.get())
        self.destroy()

    def cancel(self):
        self.info = None
        self.destroy()

    def __call__(self):
        return self.info






