import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Use ttk for themed widgets
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
    screen_height = root.winfo_screenheight()

    # Set initial window size to 600px width and 80% of the screen height
    window_width = 600
    window_height = int(screen_height * 0.8)

    # Set the initial size and limit the maximum width to 600px
    root.geometry(f"{window_width}x{window_height}")
    root.minsize(300, 300)  # Allow resizing smaller
    root.maxsize(600, window_height)  # Limit maximum width to 600px


# Create the main window
root = tk.Tk()
root.title("Mood Journal")
set_window_size(root)

# Set up grid configuration for root window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Define common styles for all widgets
main_font = ("Helvetica", 12)
heading_font = ("Helvetica", 14, "bold")

# Colors based on your preferences
app_bg_color = "#000000"  # Background color for the whole app
text_color = "#ffffff"  # Text color for titles and inputs
input_bg_color = "#333333"  # Background color for the input fields
button_bg_color = "#123456"  # Button background color (lightblue)
button_text_color = "#fff"  # Button text color (white and bold)

# Apply the background color to the entire window
root.configure(bg=app_bg_color)

# Create the main frame with padding for centering
main_frame = tk.Frame(root, padx=20, pady=20, bg=app_bg_color)
main_frame.grid(row=0, column=0, sticky="nsew")

# Configure main_frame to expand and fill available space
main_frame.grid_columnconfigure(0, weight=1)

# Display the current time in the user's local timezone
tk.Label(main_frame, text="Time:", font=heading_font, bg=app_bg_color, fg=text_color).grid(row=0, column=0, pady=5, sticky="ew")
time_label = tk.Label(main_frame, text=datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S"), relief="sunken", font=main_font, bg=input_bg_color, fg=text_color)
time_label.grid(row=1, column=0, pady=5, sticky="ew")

# Mood entry field (free text)
tk.Label(main_frame, text="Enter Your Mood:", font=heading_font, bg=app_bg_color, fg=text_color).grid(row=2, column=0, pady=5, sticky="ew")
mood_entry = tk.Entry(main_frame, font=main_font, bg=input_bg_color, fg=text_color)
mood_entry.grid(row=3, column=0, pady=5, sticky="ew")

# Journal entry box
tk.Label(main_frame, text="Journal Entry:", font=heading_font, bg=app_bg_color, fg=text_color).grid(row=4, column=0, pady=5, sticky="ew")
entry_box = tk.Text(main_frame, height=10, font=main_font, bg=input_bg_color, fg=text_color)
entry_box.grid(row=5, column=0, pady=5, sticky="ew")

# Configure ttk Style for buttons
style = ttk.Style()
style.configure("TButton",
                background=button_bg_color,
                foreground=button_text_color,
                font=("Helvetica", 12, "bold"))

# Submit button (styled using ttk.Button)
submit_button = ttk.Button(main_frame, text="Save Entry", command=save_entry, style="TButton")
submit_button.grid(row=6, column=0, pady=20, sticky="ew")

# Button to display mood trends (also ttk.Button)
trend_button = ttk.Button(main_frame, text="Show Mood Trends", command=lambda: show_mood_trends(period="monthly"), style="TButton")
trend_button.grid(row=7, column=0, pady=10, sticky="ew")

# Start the Tkinter loop
root.mainloop()
