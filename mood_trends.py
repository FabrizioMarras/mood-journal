import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import os

# Load mood journal data from the JSON file
def load_mood_data():
    if os.path.exists("mood_journal.json"):
        with open("mood_journal.json", "r") as file:
            return json.load(file)
    else:
        return []

# Process data to group moods by week or month
def process_mood_data(data, period="weekly"):
    mood_counts = {}

    for entry in data:
        # Convert date string to datetime object
        entry_date = datetime.strptime(entry["date"], "%Y-%m-%d")

        # Determine the grouping key (week or month)
        if period == "weekly":
            group_key = entry_date.strftime("%Y-%W")  # Year-Week
        elif period == "monthly":
            group_key = entry_date.strftime("%Y-%m")  # Year-Month
        else:
            raise ValueError("Invalid period. Choose 'weekly' or 'monthly'.")

        # Create the group if it doesn't exist
        if group_key not in mood_counts:
            mood_counts[group_key] = []

        # Add the mood to the corresponding group
        mood_counts[group_key].append(entry["mood"])

    # Convert mood lists to mood counts
    mood_trends = {key: Counter(moods) for key, moods in mood_counts.items()}
    return mood_trends

# Plot mood trends over time
def plot_mood_trends(mood_trends, period="weekly"):
    # Extract time periods and unique moods
    periods = sorted(mood_trends.keys())
    all_moods = set()
    for counts in mood_trends.values():
        all_moods.update(counts.keys())

    # Prepare the data for plotting
    mood_data = {mood: [] for mood in all_moods}

    for period in periods:
        counts = mood_trends[period]
        for mood in all_moods:
            mood_data[mood].append(counts.get(mood, 0))  # 0 if mood not present

    # Plot the data
    plt.figure(figsize=(10, 6))
    for mood, values in mood_data.items():
        plt.plot(periods, values, label=mood, marker='o')

    plt.title(f"Mood Trends ({period.capitalize()})")
    plt.xlabel("Time Period")
    plt.ylabel("Mood Count")
    plt.xticks(rotation=45)
    plt.legend(title="Moods")
    plt.tight_layout()
    plt.show()

# Main function to load, process, and plot the data
def show_mood_trends(period="monthly"):
    data = load_mood_data()
    if not data:
        print("No data available.")
        return

    mood_trends = process_mood_data(data, period=period)
    plot_mood_trends(mood_trends, period=period)
