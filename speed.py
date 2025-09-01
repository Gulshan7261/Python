from tkinter import *
import speedtest

# Speed Test Function
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

# Restart Function (resets both values)
def restart():
    lab_down.config(text="00")
    lab_up.config(text="00")
    speedcheck()    #re-run the test after reset

# GUI Window
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="blue")

# Heading Label
heading = Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="blue", fg="white")
heading.place(x=60, y=40, height=50, width=380)

# Download Speed
download_text = Label(sp, text="Download Speed", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
download_text.place(x=60, y=130, height=40, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 20, "bold"), bg="white")
lab_down.place(x=60, y=180, height=40, width=380)

# Upload Speed
upload_text = Label(sp, text="Upload Speed", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
upload_text.place(x=60, y=260, height=40, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 20, "bold"), bg="white")
lab_up.place(x=60, y=310, height=40, width=380)

# Button: Check Speed
button = Button(sp, text="Check Speed", font=("Times New Roman", 20, "bold"), bg="red", fg="white", command=speedcheck)
button.place(x=60, y=400, height=50, width=380)

# Button: Restart
restart_btn = Button(sp, text="Restart", font=("Times New Roman", 20, "bold"), bg="green", fg="white", command=restart)
restart_btn.place(x=60, y=480, height=50, width=380)

# Run the App
sp.mainloop()
