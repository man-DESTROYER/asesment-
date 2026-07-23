import tkinter as tk 

root = tk.Tk()
root.title("Control interface Alpha")
root.geometry("500x700")

root.title("Save Entries")


result_label = tk.Label(root, text="insert time here")
result_label.pack()

information_label = tk.Label(root, text="what does insert time here mean? \n this button saves your time that you have selected for later.\n When the time you have selected has come it will tell you that your time is soon ariving")
information_label.pack()

information_label = tk.Label(root, text="What is the purpose of haveing this window? \n This window helps users who have less time than others. \n this helps with people rembering things they easliy forget what they are surpost to do")
information_label.pack()


go_button = tk.Button(root, text="Go")      # CORRECTcommand=run)add comand later

def greet():
    name = name_entry.get()                          # read the input
    result_label.config(text="Kia ora " + name)      # produce output on screen

def on_enter(event):                  # bound functions receive an event
    print("Enter was pressed")

root.title("Listbox demo")

fruit_listbox = tk.Listbox(root)
fruit_listbox.pack(padx=10, pady=10)
for fruit in ["Apple", "Banana", "Kiwi"]:
    fruit_listbox.insert(tk.END, fruit)   # add items at the end

result_label = tk.Label(root, text="")
result_label.pack()


def show_selected():
    selected = fruit_listbox.curselection()   # tuple of indexes, e.g. (0,)
    if selected:
        result_label.config(text="Picked: " + fruit_listbox.get(selected[0]))


show_button = tk.Button(root, text="Show selected", command=show_selected)
show_button.pack(pady=5)




name_entry = tk.Entry(root)
name_entry.pack()
name_entry.bind("<Return>", on_enter)
greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()

def add_item(item):
    item_listbox.insert(tk.END, item)


apple_button = tk.Button(root, text="Add Apple",
                         command=lambda: add_item("Apple"))
apple_button.pack()

def show():
    # .get() reads the text — always a string
    result_label.config(text="You typed: " + name_entry.get())


show_button = tk.Button(root, text="click me", command=show)
show_button.pack(pady=5)

root.mainloop()









