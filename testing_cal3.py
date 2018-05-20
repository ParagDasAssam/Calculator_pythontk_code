import ast
from tkinter import *

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4,bg="pink")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self,
              relief=RIDGE,
              textvariable=display,
              justify='right',
              bd=30,
              bg="pink").pack(side=TOP, expand=YES, fill=BOTH)

        for button_text in ("CE", "C"):
            erase = iCalc(self, TOP)
            button(erase, LEFT, button_text,
                   lambda storeObj=display, q=button_text: storeObj.set(''))

        for row in ("789 /" , "456*" , "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            # renamed button_text here, too.
            for button_text in row:
                button(FunctionNum, LEFT, button_text,
                        lambda storeObj=display, q=button_text: storeObj.set(storeObj.get() + q))

        EqualsButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualsButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                                lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals = button(EqualsButton, LEFT, iEquals,
                    lambda storeObj=display, s=' %s '%iEquals: storeObj.set(storeObj.get()+s))

    def calc(self, display):
        try:
            display.set(ast.literal_eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    app().mainloop()
