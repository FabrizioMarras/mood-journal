import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tzlocal import get_localzone
import json
import os
from mood_trends import show_mood_trends

# Get the local timezone of the user
local_timezone = get_localzone()

# Function to save the entry to a JSON file
def save_entry():
    mood = mood_entry.get().strip()  # Get text from the mood entry box
    journal_entry = entry_box.get("1.0", "end").strip()  # Get text from the entry box
    
    if not mood:
        messagebox.showwarning("Input Error", "Please enter your mood.")
        return
    if not journal_entry:
        messagebox.showwarning("Input Error", "Journal entry cannot be empty.")
        return

    # Get the current date and time in the user's local timezone
    current_time = datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a dictionary to represent the new entry
    new_entry = {
        "date": current_time.split()[0],  # Date part
        "time": current_time.split()[1],  # Time part
        "mood": mood,
        "entry": journal_entry
    }
    
    # Check if the file exists; if not, create an empty list
    if os.path.exists("mood_journal.json"):
        with open("mood_journal.json", "r") as file:
            data = json.load(file)
    else:
        data = []

    # Append the new entry to the list
    data.append(new_entry)

    # Write the updated data back to the JSON file
    with open("mood_journal.json", "w") as file:
        json.dump(data, file, indent=4)

    # Notify the user and clear the input fields
    messagebox.showinfo("Success", "Your entry has been saved.")
    mood_entry.delete(0, 'end')
    entry_box.delete("1.0", "end")

# Adjust window size based on screen size
def set_window_size(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set window size to 80% of the screen width and height
    window_width = int(screen_width * 0.8)
    window_height = int(screen_height * 0.8)

    root.geometry(f"{window_width}x{window_height}")

# Create the main window
root = tk.Tk()
root.title("Mood Journal")
set_window_size(root)

# Create a canvas for scrollable content
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Add a vertical scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

# Create a frame to contain the widgets inside the canvas
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Display the current time in the user's local timezone
tk.Label(content_frame, text="Time:").pack(pady=5)
time_label = tk.Label(content_frame, text=datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S"), relief="sunken", width=25)
time_label.pack(pady=5)

# Mood entry field (free text)
tk.Label(content_frame, text="Enter Your Mood:").pack(pady=5)
mood_entry = tk.Entry(content_frame, width=30)
mood_entry.pack(pady=5)

# Journal entry box
tk.Label(content_frame, text="Journal Entry:").pack(pady=5)
entry_box = tk.Text(content_frame, height=10, width=40)
entry_box.pack(pady=5)

# Submit button
submit_button = tk.Button(content_frame, text="Save Entry", command=save_entry)
submit_button.pack(pady=20)

# Button to display mood trends
trend_button = tk.Button(content_frame, text="Show Mood Trends", command=lambda: show_mood_trends(period="monthly"))
trend_button.pack(pady=10)

# Start the Tkinter loop
root.mainloop()
