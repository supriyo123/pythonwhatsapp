from tkinter import *

root = Tk()
def logic():
    table = enter.get()
    two = int(table)*2
    three =int(table)*3
    four = int(table) * 4
    five = int(table) * 5
    six = int(table) * 6
    seven = int(table) * 7
    eight = int(table) * 8
    nine = int(table) * 9
    ten = int(table) * 10

    labeltext.set(table + "x" + "1 = " + table)
    labeltext2.set(table + "x" + "2 = " + str(two))
    labeltext3.set(table + "x" + "3 = " + str(three))
    labeltext4.set(table + "x" + "4 = " + str(four))
    labeltext5.set(table + "x" + "5 = " + str(five))
    labeltext6.set(table + "x" + "6 = " + str(six))
    labeltext7.set(table + "x" + "7 = " + str(seven))
    labeltext8.set(table + "x" + "8 = " + str(eight))
    labeltext9.set(table + "x" + "9 = " + str(nine))
    labeltext10.set(table + "x" + "10 = " + str(ten))
Label(root, text="TABLE SOFTWTARE FOR STUDENTS", bg="red").pack()
Label(root, text="ENTER THE VALUE FOR FINDING ITS TABLE", bg="orange").pack()
enter = Entry(root)
enter.pack()
Button(root,text="Click Here", command=logic).pack()
labeltext = StringVar()
labeltext.set('----')
Label(root, textvariable=labeltext, bg="yellow").pack()
labeltext2 = StringVar()
labeltext2.set('----')
Label(root, textvariable=labeltext2, bg="orange").pack()
labeltext3 = StringVar()
labeltext3.set('----')
Label(root, textvariable=labeltext3, bg="pink").pack()
labeltext4 = StringVar()
labeltext4.set('----')
Label(root, textvariable=labeltext4, bg="purple").pack()
labeltext5 = StringVar()
labeltext5.set('----')
Label(root, textvariable=labeltext5, bg="magenta").pack()
labeltext6 = StringVar()
labeltext6.set('----')
Label(root, textvariable=labeltext6, bg="red").pack()
labeltext7 = StringVar()
labeltext7.set('----')
Label(root, textvariable=labeltext7, bg="violet").pack()
labeltext8 = StringVar()
labeltext8.set('----')
Label(root, textvariable=labeltext8, bg="blue").pack()
labeltext9 = StringVar()
labeltext9.set('----')
Label(root, textvariable=labeltext9, bg="green").pack()
labeltext10 = StringVar()
labeltext10.set('----')
Label(root, textvariable=labeltext10, bg="brown").pack()
#label.pack()

root.mainloop()


