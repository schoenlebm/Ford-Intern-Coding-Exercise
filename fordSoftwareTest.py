#Author: Michael Schoenleb
#Date: 3/16
#Purpose: Ford Software Programming Assessment, a gui that accepts a user integer input, and... 
#outputs either Mustang if that input is divisible by 3, Bronco if it is divisible by 5, MustangBronco if it is divisible by both, or just that integer if it is divisible by neither
import tkinter as tk
class mustangBroncoGUI():
    
    def __init__(self):
        self.top = tk.Tk()
        
        ##gui component set up
        #instruction label
        self.greeting = tk.Label(text="Input an integer in the entry box below, then press enter.",width=70)
        self.greeting.pack(pady=4)
        
        #number entry box
        self.entry = tk.Entry(width = 20)
        self.entry.pack(pady=4)
        
        #enter button
        self.button =tk.Button(text="Enter",command=self.mustangBroncoCallBack)
        self.button.pack(pady=4)
        
        #output area
        self.output = tk.Label()
        self.output.pack(pady=4)
        
        #calling the event loop
        self.top.mainloop()
        
        
    def mustangBroncoCallBack(self):
    
        #retrieve the user entered value
        user_input = self.entry.get()
        
        #check if the user can convert string to int, if not then return to event loop after error message
        try:
            user_input = int(user_input)
        except ValueError:
            self.output['text'] = "ERROR: Invalid input (potentially non-integer), please try again"
            return
            
        #logic for mustangBronco output
        if (user_input % 3 == 0) and (user_input % 5 == 0):
            self.output['text'] = "MustangBronco"
        elif user_input % 3 == 0:
            self.output['text'] = "Mustang"
        elif user_input % 5 == 0:
            self.output['text'] = "Bronco"
        else:
            self.output['text'] = user_input
            

mustangBroncoGUI()
