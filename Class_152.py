from tkinter import *
root=Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")
label= Label(root)


array_1d = ["Decy", "Richard", "Sky", "Shika"]
print(array_1d[0])

array_2d = [["decy", "A"], ["richard", "A"] ["sky", "B"] ["shika"," F"]]
print(array_2d[0][1])

array_3d = [["decy","A","Average"], ["richard","A","Average"] ["sky","B","Badly"] ["shika", "F" , "Failure At being able to be a good online friend"]]
print(array_3d[0][1][2])

def report():
    label["text"] = array_3d[0][1][0] + " got grade " + array_3d[0][1][1] +" and he is doing " + array_3d[0][1][2]
    
btn = Button(root, text= "show report", command = report )
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

label.place(relx = 0.5, rely =0.6, anchor = CENTER)

root.mainloop()