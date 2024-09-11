import tkinter as tk
from tkinter import messagebox
from datetime import date

# Function to save the entry
def save_entry():
    mood = mood_entry.get().strip()  # Get text from the mood entry box
    journal_entry = entry_box.get("1.0", "end").strip()  # Get text from the entry box
    
    if not mood:
        messagebox.showwarning("Input Error", "Please enter your mood.")
        return
    if not journal_entry:
        messagebox.showwarning("Input Error", "Journal entry cannot be empty.")
        return

    # Use today's date directly
    today_date = date.today().strftime("%Y-%m-%d")
    print(f"Date: {today_date}, Mood: {mood}, Entry: {journal_entry}")
    
    # Clear inputs after saving
    mood_entry.delete(0, 'end')
    entry_box.delete("1.0", "end")

# Create the main window
root = tk.Tk()
root.title("Mood Journal")
root.geometry("400x400")

# Display the auto-filled date (read-only)
tk.Label(root, text="Date:").pack(pady=5)
date_label = tk.Label(root, text=date.today().strftime("%Y-%m-%d"), relief="sunken", width=15)
date_label.pack(pady=5)

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
