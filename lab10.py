from tkinter import *
file = "marvel.txt"

def read():
    textBox.delete('1.0', END)
    file = open("marvel.txt")
    str1 = file.read()
    textBox.insert(INSERT,str1)
    print(textBox)

def calculate():
    #destroys the read part
    textBox.delete('1.0',END)
    file = open("marvel.txt")
    str1 = file.read()
    list1 = str1.split()
    unique = set(list1)
    for words in unique:
        textBox.insert(INSERT, ("freq of " + words + " is "+" ---> "+str(list1.count(words))+ "\n"))
        textBox.pack(side = LEFT,expand =True)

    sb = Scrollbar(frame)
    sb.pack(side =RIGHT,fill=BOTH)

    textBox.config(yscrollcommand=sb.set)
    sb.config(command = textBox.yview)

    frame.pack(expand = True)



root = Tk()

root.title("my project")

frame = LabelFrame(root,text="my words")
frame.pack()

textBox = Text(frame)
textBox.pack()

button1 = Button(frame,text="READ",command = read)
button1.pack()

button2 = Button(frame,text = "CALCULATE",command = calculate)
button2.pack()
root.mainloop()
