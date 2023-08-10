import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(window, font=('Arial', 80), fg='black', bg='white')
clock_label.pack(padx=50, pady=50)

# Start updating the time
update_time()

# Run the application
window.mainloop()
