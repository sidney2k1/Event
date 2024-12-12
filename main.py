from tkinter import *
window=Tk()
window.title("Click")
window.geometry("400x300")
def handlekeypress(event):
    #press the character associated to the key press
    print(event.char)
window.bind("<Key>",handlekeypress)
def handleclick(event):
    print("The button was clicked")
button=Button(text="Click me")
button.pack()
button.bind("<Button-1>",handleclick)
window.mainloop()