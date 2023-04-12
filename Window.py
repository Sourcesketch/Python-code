import tkinter as tk
from tkinter import ttk

def button_fun():
    output_string.set('Hello World')

# create a window
window=tk.Tk()
window.title('Window and Widgets')
window.geometry('800x600')

#create widgets
label=tk.Text(master = window)
label.pack()

# ttk widgets
text=ttk.Label(master=window, text= 'This is text')
text.pack()

# ttk entry
entry=ttk.Entry(master=window)
entry.pack()

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Poppin 14', textvariable=output_string)
output_label.pack(pady=10)

# ttk button
button=ttk.Button(master=window, text='Click here', command = button_fun)
button.pack()

# run
window.mainloop()