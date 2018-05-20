from tkinter import*
import tkinter.messagebox

def beenClicked():
    radioValue = relStatus.get()
    tkinter.messagebox.showinfo("you clicked", radioValue)
    return
def changeLabel():
    name= "Thanks for the click " + yourName.get()
    labelText.set(name)
    yourName.delete(0,END)
    yourName.insert(0, "My name is parag")
    return

app = Tk()
app.title("GUI EXAMPLE")
app.geometry('450x300+200+200')

labelText = StringVar()
labelText.set("Click button")
label1 = Label(app, textvariable=labelText, height=4)
label1.pack()

checkBoxVal = IntVar()
checkBox1 = Checkbutton(app, variable = checkBoxVal, text="Happy?")
checkBox1.pack()

custName = StringVar(None)
yourName = Entry(app, textvariable=custName)
yourName.pack()

relStatus = StringVar()
relStatus.set(None)
radio1 = Radiobutton(app, text="Single", value="Single", variable = relStatus, command=beenClicked).pack()
radio1 = Radiobutton(app, text="Married", value="Married", variable = relStatus, command=beenClicked).pack()

button1 = Button(app, text="Click Here", width=20, command=changeLabel)
button1.pack(side='bottom', padx=15, pady=15)

app.mainloop()
