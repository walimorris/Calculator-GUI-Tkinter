#Note: Simple calculator. User has the ability to completely utilize buttons for calculations or type within the calculation entry box itself.
#After typing calculations, user will have to press the 'equals' button on GUI to calculate entry. OFF simply exits. 

from tkinter import *


class Calculator:
    
    def getReplace(self): #replace 'x' with '*' and '//' with '/', this way 'x' doesn't cause an error and '/' returns int rather than float
        self.expression = self.calcEntry.get() #Recieve entry from calculation from entry box
        self.newtext = self.expression.replace('/', '//')
        self.newtext = self.newtext.replace('x', '*')
        
    def equals(self): #when equal button is pressed, evaluate calculations, if error, delete and return error text. Else, delete calculations and return value
        self.getReplace()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.calcEntry.delete(0, END)
            self.calcEntry.insert(0, 'ERROR!')
        else:
            self.calcEntry.delete(0, END)
            self.calcEntry.insert(0, self.value)
    
    def clearAll(self): #when clear button is pressed
        self.calcEntry.delete(0, END)
        
    def action(self, argi): #button's value is inserted within calculations entrybox
        self.calcEntry.insert(END, argi)
        
    
    
    def __init__(self, master):
        self.master = master
        master.title("MATHS")
        master.configure(background="gray30")
        master.resizable(width=False, height=False)
        
        #Build widgets. Create output window for calculations
        #To expland widgets pass columns and rows, columnspan= and rowspan= then modify height and width of widget (zero button, equals button)
        self.calcEntry = Entry(master, background="gray85", relief=RIDGE) #Calculation output window
        self.offButton = Button(master, width=2, height=1, bg="red3", text="OFF", command= lambda: self.action(exit()), font="fixedsys") #Off Button
        self.buttonSeven = Button(master, width=2, height=1, bg="gray80", text="7", command= lambda: self.action(7), font="fixedsys") #Button #7
        self.buttonFour = Button(master, width=2, height=1, bg="gray80", text="4", command= lambda: self.acton(4), font="fixedsys") #Button #4
        self.buttonOne = Button(master, width=2, height=1, bg="gray80", text="1", command= lambda: self.action(1), font="fixedsys") # Button #1
        self.buttonZero = Button(master, width=10, height=2, bg="gray80", text="0", command= lambda: self.action(0), font="fixedsys") # Button #0
        self.buttonClear = Button(master, width=2, height=1, bg="yellow", text="AC", command= lambda: self.clearAll(), font="fixedsys") # Clear Button
        self.buttonEight = Button(master, width=2, height=1, bg="gray80", text="8", command= lambda: self.action(8), font="fixedsys") #Button 8
        self.buttonFive = Button(master, width=2, height=1, bg="gray80", text="5", command= lambda: self.action(5), font="fixedsys") #Buttpn #5
        self.buttonTwo = Button(master, width=2, height=1, bg="gray80", text="2", command= lambda: self.action(2), font="fixedsys") #Button #2
        self.buttonDiv = Button(master, width=2, height=1, bg="orange", text="/", command= lambda: self.action('/'), font="fixedsys") #Division Button
        self.buttonNine = Button(master, width=2, height=1, bg="gray80", text="9", command= lambda: self.action(9), font="fixedsys") #Button #9
        self.buttonSix = Button(master, width=2, height=1, bg="gray80", text="6", command= lambda: self.action(6), font="fixedsys") #Button #6
        self.buttonThree = Button(master, width=2, height=1, bg="gray80", text="3", command= lambda: self.action(3), font="fixedsys") #Button #3
        self.buttonPoint = Button(master, width=2, height=1, bg="gray80", text=".", command= lambda: self.action('.'), font="fixedsys") #Point Button
        self.buttonMultiply = Button(master, width=2, height=1, bg="orange", text="x", command= lambda: self.action('*'), font="fixedsys") #Multiply Button
        self.buttonSubtract = Button(master, width=2, height=1, bg="orange", text="-", command= lambda: self.action('-'), font="fixedsys") #Subtract Button
        self.buttonAdd = Button(master, width=2, height=1, bg="orange", text="+", command= lambda: self.action('+'), font="fixedsys") #Add Button
        self.buttonEquals = Button(master, width=2, height=4, bg="green2", text="=", command=lambda: self.equals(), font="fixedsys") #Equals Button
        
        #Place widget layout
        self.calcEntry.grid(row=0, column=1, columnspan=4, sticky=N+S+E+W, padx=15, pady=15, ipady=15) #Calculation output layout
        self.offButton.grid(row=1, column=1, sticky=W, padx=15) #Off Button layout
        self.buttonSeven.grid(row=2, column=1, sticky=W, padx=15, pady=15) #Button #7 layout
        self.buttonFour.grid(row=3, column=1, sticky=W, padx=15) #Button #4 layout
        self.buttonOne.grid(row=4, column=1, sticky=W, padx=15, pady=15) #Button #1 layout
        self.buttonZero.grid(row=5, column=1, columnspan=2, rowspan=2, sticky=W, padx=15, pady=15) #Button #0 layout
        self.buttonClear.grid(row=1, column=2, sticky=W, padx=15) #Clear Button layout
        self.buttonEight.grid(row=2, column=2, sticky=W, padx=15, pady=15) #Button #8 layout
        self.buttonFive.grid(row=3, column=2, sticky=W, padx=15) #Button #5 layout
        self.buttonTwo.grid(row=4, column=2, sticky=W, padx=15, pady=15) #Button #2 layout
        self.buttonDiv.grid(row=1, column=3, sticky=W, padx=15) #Division Button layout
        self.buttonNine.grid(row=2, column=3, sticky=W, padx=15, pady=15) #Button #9 layout
        self.buttonSix.grid(row=3, column=3, sticky=W, padx=15) #Button #6 layout
        self.buttonThree.grid(row=4, column=3, sticky=W, padx=15, pady=15) #Button #3 layout
        self.buttonPoint.grid(row=5, column=3, sticky=W, padx=15, pady=15) #Point Button layout
        self.buttonMultiply.grid(row=1, column=4, sticky=W, padx=15) #Multiply Button
        self.buttonSubtract.grid(row=2, column=4, sticky=W, padx=15, pady=15) #Subtract Button
        self.buttonAdd.grid(row=3, column=4, sticky=W, padx=15) #Add Button 
        self.buttonEquals.grid(row=4, column=4, rowspan=2, sticky=W, padx=15) #Equals Button
        
    
           
window = Tk()
myCalc = Calculator(window)
window.mainloop()
