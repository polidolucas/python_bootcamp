import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x300")
        
        self.time_left = 0
        self.running = False
        
        self.label = tk.Label(root, text="Enter time in seconds:", font=("Helvetica", 14))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=("Helvetica", 14))
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer, font=("Helvetica", 14))
        self.stop_button.pack(pady=5)
        
        self.time_label = tk.Label(root, text="Time left: 0", font=("Helvetica", 14))
        self.time_label.pack(pady=10)
    
    def start_timer(self):
        try:
            self.time_left = int(self.entry.get())
            self.running = True
            self.update_timer()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")
    
    def stop_timer(self):
        self.running = False
    
    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.time_label.config(text="Time's up!")
            self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()