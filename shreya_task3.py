import tkinter as tk




root = tk.Tk()
root.title("Shreya's Calculator")
root.geometry('300x400')

expression = ""
entry_var = tk.StringVar()

entry = tk.Entry(root, textvar=entry_var, font='Arial 20', justify='right')
entry.pack(fill='both', ipadx=8, pady=10, padx=10)
root.mainloop()