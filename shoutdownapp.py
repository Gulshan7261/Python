from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_Time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -1")  #logout ke liye -1 use hota hai 

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("shutdown App")
st.geometry("500x500")
st.config(bg="blue")

# Restart Button
r_button = Button(st, text="Restart", font=("Time New Roman", 20 ,"bold"),
    relief=RAISED, cursor="plus",command=restart)
r_button.place(x=180,y=60,height=50,width=150)
 
# Restart with Time Button
 
rt_button = Button(st, text="Restart Time", font=("Time New Roman", 20,"bold"),
    relief=RAISED,cursor="plus",command=restart_Time)
rt_button.place(x=160,y=150,height=50,width=200)

# log Out Button
l_button = Button(st, text="Log-Out", font=("Time New Roman",20, "bold"),
    relief=RAISED,cursor="plus",command=logout)
l_button.place(x=180,y=240,height=50,width=150)

# shutDown Button
s_button = Button(st, text="ShutDown", font=("Time New Roman",20, "bold"),
    relief=RAISED,cursor="plus",command=shutdown)
s_button.place(x=170,y=330,height=50,width=170)

st.mainloop()

