import tkinter as tk
from tkinter import messagebox

def update_timer():
    global time_remaining
    if time_remaining > 0:
        mins, secs = divmod(time_remaining, 60)
        timer_label.config(text=f'{mins:02d}:{secs:02d}')
        time_remaining -= 1
        root.after(1000, update_timer)
    else:
        messagebox.showinfo("Time's Up!", "The countdown has finished.")

def start_timer():
    global time_remaining
    input_minutes = entry.get()
    try:
        minutes = int(input_minutes)
        time_remaining = minutes * 60
        update_timer()
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Countdown Timer")

time_remaining = 0

timer_label = tk.Label(root, text="", font=("Helvetica", 48))
timer_label.pack(padx=20, pady=20)

entry = tk.Entry(root, font=("Helvetica", 24))
entry.pack(padx=20, pady=10)

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

root.mainloop()
