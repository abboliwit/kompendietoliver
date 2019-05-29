from tkinter import *
import keyboard
#while True:
   # if keyboard.is_pressed('esc'):
   #     print ("escape")
List = [3,2,4,5]
list2 = [2,2,3,4]
print(List)
List = list2
print(List)
def hello (boi):
    if boi[1]==2:
        return True
    else:
        return False

if hello(List) == True:
    print("you are not stupid")
# master = Tk()
# def opt():
#     print("Options")

# C = Canvas(master,bg="#000000",height=690,width=900)
# C.pack()
# C.pack_propagate(0)
# C.update()
# o= Button(C, command = opt, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Options",fg="#ffffff")
# o.pack()
# C.update()

# mainloop()