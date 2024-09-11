import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tzlocal import get_localzone  # Automatically detect the user's timezone
import json
import os

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

# Create the main window
root = tk.Tk()
root.title("Mood Journal")
root.geometry("400x400")

# Display the current time in the user's local timezone
tk.Label(root, text="Time:").pack(pady=5)
time_label = tk.Label(root, text=datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S"), relief="sunken", width=25)
time_label.pack(pady=5)

# Mood entry field (free text)
tk.Label(root, text="Enter Your Mood:").pack(pady=5)
mood_entry = tk.Entry(root, width=30)
mood_entry.pack(pady=5)

# Journal entry box
tk.Label(root, text="Journal Entry:").pack(pady=5)
entry_box = tk.Text(root, height=10, width=40)
entry_box.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Save Entry", command=save_entry)
submit_button.pack(pady=20)

# Start the Tkinter loop
root.mainloop()
