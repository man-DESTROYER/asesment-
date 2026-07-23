import tkinter as tk 

root = tk.Tk()
root.title("Control interface Alpha")
root.geometry("600x400")

root.title("Save Entries")


result_label = tk.Label(root, text="insert time here")
result_label.pack()

information_label = tk.Label(root, text="what does insert time here mean? \n this button saves your time that you have selected for later.\n When the time you have selected has come it will tell you that your time is soon ariving")
information_label.pack()

information_label = tk.Label(root, text="What is the purpose of haveing this window? \n This window helps users who have less time than others. \n this helps with people rembering things they easliy forget what they are surpost to do")
information_label.pack()


def show():
    # .get() reads the text — always a string
    result_label.config(text="You typed: " + name_entry.get())


show_button = tk.Button(root, text="click me", command=show)
show_button.pack(pady=5)

root.mainloop()









