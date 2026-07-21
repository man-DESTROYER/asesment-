import tkinter as tk 

root = tk.Tk()
root.title("Control interface Alpha")
root.geometry("400x400")

root.title("Save Entries")

def save_data():
    text = name_entry.get()

    # Save to file
    with open("data.txt", "a") as file:
        file.write(text + "\n")

    # Reload everything from the file and display it
    with open("data.txt", "r") as file:
        result_label.config(text=file.read())

    # Clear the entry box
    name_entry.delete(0, tk.END)

name_entry = tk.Entry(root)
name_entry.pack()

save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

# Show previously saved entries when the program starts


root.mainloop()









