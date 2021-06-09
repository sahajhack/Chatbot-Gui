from tkinter import *
grey="grey"
mycolor1 = '#555555'
mycolor2 = '#242424'
mycolor3 = '#00AAFF'
root = Tk()
root.title("HackDude")
root.geometry("400x500")
root.resizable(0, 0)
root.config(bg=mycolor1)
root.wait_visibility(root)
root.wm_attributes('-alpha',0.95)
root.attributes('-alpha', 0.95)

#create a chat window
chatWindow = Text(root, bd=3, bg='black', fg='white', width=50, height=50)
chatWindow.place(x=5, y=5, height= 435, width=390)

#create a message window
msgWindow = Text (root, bd=1, bg=mycolor2,fg=mycolor3, width=50, height=50)
msgWindow.place(x=5, y=445, height=50, width=295)

btn = Button (root, text='send', bg=mycolor2, activebackground=mycolor2, fg=mycolor3, width=50, height=50)
btn.place(x=301, y=445, height=50, width=94)


        


root.mainloop()