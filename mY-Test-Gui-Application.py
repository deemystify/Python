from tkinter import *


window=Tk()
window.geometry("300x300")
window.title("Welcome to Lloyd's Application")
label1 = Label(window, text="Welcome to Lloyd's Application", fg="Blue", bg="yellow", relief="solid", font=("arial", 12, "bold"))
#label1.pack(fill=BOTH, pady=2,padx=2, expand=True)
#label1.place(x=110, y=80)
#label1.grid(row=1,column=1)
label1.pack()

#Button variable.

button1 = Button(window, text="Click to Begin", fg="black",bg="white", relief= RAISED, font=("arial", 12, "bold"))
#button1.place(x=110,y=110)
button1.pack()
#country = input ('What country do you live in? ')



window.mainloop()