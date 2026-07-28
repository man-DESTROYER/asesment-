import tkinter as tk 
from tkinter import messagebox
from time import strftime
root = tk.Tk()
root.title("Control interface Alpha")
root.geometry("500x700")

root.title("Save Entries")

#messagebox.showinfo("information", "what does insert time here mean? \n this button saves your time that you have selected for later.\n When the time you have selected has come it will tell you that your time is soon ariving soon\nWhat is the purpose of haveing this window? \n This window helps users who have less time than others. \n this helps with people rembering things they easliy forget what they are surpost to do")

result_label = tk.Label(root, text="insert time here")
result_label.pack()

hour_list =["12", "1", "2" ,"3","4","5","6","7","8","9","10","11"]
minutes_list = ["00","15", "30","45"]
am_pm_list = ["AM", "PM"]

hour_value = tk.StringVar(root)
minutes_value = tk.StringVar(root)
am_pm_value = tk.StringVar(root)

hour_menu = tk.OptionMenu(root,hour_value, *hour_list)
hour_menu.pack()
minutes_menu = tk.OptionMenu(root,minutes_value, *minutes_list)
minutes_menu.pack()
am_pm_menu = tk.OptionMenu(root,am_pm_value, *am_pm_list)
am_pm_menu.pack()








def on_enter(event):                  # bound functions receive an event
    add_to_list()
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)



root.title("Listbox demo")

time_listbox = tk.Listbox(root, width=50)
time_listbox.pack(padx=10, pady=10)


result_label = tk.Label(root, text="")
result_label.pack()


def add_to_list():
    #selected = fruit_listbox.curselection()   # tuple of indexes, e.g. (0,)
   
    if name_time.get() != "":
        time_listbox.insert(tk.END, name_time.get() + " Due by" + hour_value.get() + minutes_value.get() + am_pm_value.get())   # add items at the end


show_button = tk.Button(root, text="time inserted", command=add_to_list)
show_button.pack(pady=5)




name_time = tk.Entry(root)
name_time.pack()
name_time.bind("<Return>", on_enter)

result_label = tk.Label(root, text="")
result_label.pack()

lbl = tk.Label(root, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()




root.mainloop()









