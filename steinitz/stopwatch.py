from tkinter import Label

class Stopwatch(Label):
    def __init__(self, count=0,  **args):
        Label.__init__(self, **args)
        self.sched(count)
        self.isstopped = True

    def run(self):
        if not self.isstopped:
            self.after(1000, self.run)
        self.dec(1)

    def start(self):
        self.isstopped = False
        self.run()

    def stop(self):
        self.isstopped = True

    def format(self, time):

        hour = time // 60 ** 2
        min = (time - hour * 60 ** 2) // 60
        sec = time - (hour * 60 ** 2 + min * 60) 

        return hour, min, sec


    def inc(self, count):
        self.count = self.count + count
        self.sched(self.count)

    def dec(self, count):
        self.count = self.count - count
        self.sched(self.count)

    def sched(self, count):
        self.count = count

        formated = self.format(self.count)
        data = '%02d:%02d:%02d' % formated 

        self.configure(text=data)
