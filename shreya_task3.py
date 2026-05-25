import tkinter as tk

def click(event):
    pass


root = tk.Tk()
root.title("Shreya's Calculator")
root.geometry('300x400')

expression = ""
entry_var = tk.StringVar()

entry = tk.Entry(root, textvar=entry_var, font='Arial 20', justify='right')
entry.pack(fill='both', ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0","C","=","+"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(expand=True, fill='both')
    for btn in row:
        b = tk.Frame(button_frame, text=btn, font='Arial 18', relief='ridge', width=5, height=2)
        b.pack(side='left', expand=True, fill='both')
        b.bind('<Button-1>', click)
root.mainloop()