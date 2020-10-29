import tkinter
from tkinter import messagebox
class KiloConverter:
    def __init__(self):
        
        self.root = tkinter.Tk()
       
        self.top_frame = tkinter.Frame(self.root)
        self.bottom_frame = tkinter.Frame(self.root)
        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter distance in Kilometers: ')
        self.entry = tkinter.Entry(self.top_frame, width = 10)
        
        self.prompt_label.pack(side = 'left')
        self.entry.pack(side = 'left')
        
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.root.destroy)
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
        
    def convert(self):
        kilo = float(self.entry.get())
        miles = kilo * 0.6214
        messagebox.showinfo('Results', str(kilo)+ ' kilometers is equal to ' + str(miles) + ' miles')
gui = KiloConverter()      
