from tkinter import Toplevel, RAISED, Frame, Scrollbar, Y, Text, Entry, X, BOTH, MOVETO, Tk, END

class Chat(Toplevel):
    def __init__(self, root, send, title, username='me'):
        Toplevel.__init__(self, root)
        self.send     = send
        self.root     = root
        self.username = username
        self.title(title)

        self.frame1    = Frame(self, border=3, relief=RAISED, padx=5, pady=5)
        self.scrollbar = Scrollbar(master=self.frame1)
        self.scrollbar.pack(side='right', fill=Y)

        self.text = Text(self.frame1, yscrollcommand=self.scrollbar.set, font=('Helvetica', 8))

        self.scrollbar.config(command=self.text.yview)


        self.frame2 = Frame(self, border=3, relief=RAISED, padx=5, pady=5)

        self.entry = Entry(self.frame2)
        self.entry.pack(fill=X)

        self.frame2.pack(side='bottom', fill=X)
        self.frame1.pack(side='top', expand=True, fill=BOTH)
        self.text.pack(side='top', expand=True, fill=BOTH)

        self.entry.bind('<KeyPress-Return>', self.send_msg)


    def update_text(self, data):
        self.text.insert(END, '%s\n' % data)
        self.text.yview(MOVETO, 1.0)

    def send_msg(self, widget):
        data = self.entry.get()
        self.update_text('<%s>%s' % (self.username, data))
        self.entry.delete(0, END)
        self.send(data)

if __name__ == '__main__':
    root = Tk()
    chat = Chat(root)
    root.mainloop()




