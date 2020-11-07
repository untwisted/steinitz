from tkinter import Toplevel, Frame, RAISED, Label, Entry, END, E, BOTH, Button

class AskRating(Toplevel):
    def __init__(self, root, con):
        self.root = root
        self.con = con

        Toplevel.__init__(self, master=root)


        self.protocol('WM_DELETE_WINDOW', self.cancel)

        self.title('Rating Range')
        self.transient(self.root)

        self.resizable(height=False, width=False)

        self.frame1 = Frame(master=self, padx=5, pady=5, border=3, relief=RAISED)

        self.label1 = Label(master=self.frame1, text='Min Blitz rating:')
        self.entry1 = Entry(master=self.frame1)
        self.entry1.insert(END, '1300')

        self.label2 = Label(master=self.frame1, text='Max Blitz rating:')
        self.entry2 = Entry(master=self.frame1)
        self.entry2.insert(END, '1700')

        self.label3 = Label(master=self.frame1, text='Min Standard rating:')
        self.entry3 = Entry(master=self.frame1)
        self.entry3.insert(END, '1600')

        self.label4 = Label(master=self.frame1, text='Max Standard rating:')
        self.entry4 = Entry(master=self.frame1)
        self.entry4.insert(END, '1900')


        self.label1.grid(row=0, column=0, sticky=E)
        self.entry1.grid(row=0, column=1, sticky=E)

        self.label2.grid(row=1, column=0, sticky=E)
        self.entry2.grid(row=1, column=1, sticky=E)

        self.label3.grid(row=2, column=0, sticky=E)
        self.entry3.grid(row=2, column=1, sticky=E)

        self.label4.grid(row=3, column=0, sticky=E)
        self.entry4.grid(row=3, column=1, sticky=E)
        self.frame1.pack(side='top', fill=BOTH)

        self.frame2 = Frame(master=self, padx=5, pady=5, border=3, relief=RAISED)
        self.button1 = Button(master=self.frame2,text='Ok', command=self.ok)
        self.button2 = Button(master=self.frame2,text='Cancel', command=self.cancel)
        self.button1.pack(side='left', expand=True, fill=BOTH)
        self.button2.pack(side='left', expand=True, fill=BOTH)
        self.frame2.pack(side='top', fill=BOTH)
        self.root.wait_window(self)

    def ok(self):
        (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get())

        self.con.send_cmd('set formula blitz=1 && rating>=%s && rating<=%s || standard=1 && rating>=%s && rating<=%s\r\n' % 
                     (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get()))
        self.destroy()

    def cancel(self):
        self.destroy()

    def __call__(self):
        return self.value









