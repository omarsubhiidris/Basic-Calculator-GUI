from tkinter import *
root = Tk()
#App icon
img = PhotoImage(file='F:\\ARK\\مشروع التخرج\\Calculator\\UI_assets_clip_content\\Calculator.png')
root.iconphoto(False, img)
#App title
root.title('x')
#App dimensions
root.geometry("203x313")
#Fixed dimensions app
root.resizable(width=0, height=0)
#App background
root.configure(bg="#5E5D5D")

#Calculator screen
e= Entry(root,width=50,font="Roboto 35",bg="#EEF5F3")
e.pack()

# Load button image
button_images = [
    PhotoImage(file=f"F:\\ARK\\مشروع التخرج\\Calculator\\UI_assets_clip_content\\Frame {i+1}.png")
    for i in range(19)
]
# Button coordinates (5 rows × 4 columns)
coordinates = [
(0, 60), (50, 60), (100, 60), (150, 60),
    (0, 110), (50, 110), (100, 110), (150, 110),
    (0, 160), (50, 160), (100, 160), (150, 160),
    (0, 210), (50, 210), (100, 210), (150, 210),
    (0, 260), (100, 260), (150, 260)]

# Create 19 buttons
button_values = [
    "DEL", "+-", "AC", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "="
]

# Return values
def click(value):
    if value == "AC":   
        e.delete(0, END)
    elif value == "DEL":  
        e.delete(len(e.get()) - 1, END)
    elif value == "=": 
        try:
            expression = e.get().replace("×", "*").replace("÷", "/")  
            result = eval(expression)
            e.delete(0, END)
            e.insert(END, str(result)) 
        except:
            e.delete(0, END)
            e.insert(END, "Error") 
    elif value == "+-": 
         current_text = e.get()
         if current_text:
            if current_text[0] == "-":
                e.delete(0)
            else:
                e.insert(0, "-")

    else:
        e.insert(END, value)  

# UI 
buttons = []
for i in range(19):
    btn = Button(root, background="#5E5D5D", image=button_images[i], borderwidth=0, 
                 command=lambda i=i: click(button_values[i]))  # يرسل الرقم الصحيح
    btn.place(x=coordinates[i][0], y=coordinates[i][1])
    buttons.append(btn)

root.mainloop()

