# Mood Journal

## Overview
Mood Journal is a simple desktop application built with Python and Tkinter. The app allows users to record their daily moods along with journal entries. Each entry is timestamped with the current date and time and saved to a JSON file for future reference. The application includes features for submitting mood entries and viewing trends over time.

- Log daily moods (happy, sad, neutral, etc.) with notes.
- Display graphs showing mood trends over weeks or months.
- Include a simple sentiment analysis of the user's notes.

## Features

- **Mood and Journal Entry**: Users can input their current mood and a detailed journal entry.
- **Auto Timestamping**: The app automatically records the date and time of each entry.
- **Persistent Data**: All entries are saved to a mood_journal.json file, allowing users to keep a history of their moods and reflections.
- **Responsive UI**: The application dynamically resizes and adapts to the size of the window, with a maximum width of 600px to ensure a consistent layout.
- **Button Actions**: Users can submit new entries or view mood trends.

## Technologies

- **Python 3.x**: The main programming language used for this project.
- **Tkinter**: A built-in Python library used for creating the graphical user interface (GUI).
- **JSON**: Used to store the journal entries in a file for persistent data.

## Setup Instructions

### Prerequisites
Python 3.x installed on your machine.
No additional libraries are required for Tkinter as it comes built-in with Python. However, if you're using time zone support, install the tzlocal library:

```bash
pip install tzlocal
```

### How to Run

1. Clone the repository:

```bash
git clone https://github.com/FabrizioMarras/mood-journal.git
```

2. Navigate to the project folder:

```bash
cd mood-journal
```

3. Run the Python script:

```bash
python mood_journal.py
```

## Project Structure

```bash

├── mood_journal.py       # Main Python file with the Tkinter app
├── mood_trends.py        # Python file to display mood trends
├── mood_journal.json     # File where journal entries are stored
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (optional)
```

## How to Use the App

1. Start the App: 
Once you run the app, a window will appear with fields for entering your current mood and journal entry.

2. Input Fields:

- **Time**: The app automatically displays the current date and time.
- **Enter Your Mood**: Type in your current mood (e.g., Happy, Sad, Stressed, etc.).
- **Journal Entry**: Type in your reflections for the day.
- **Save Entry**: Click the "Save Entry" button to save your mood and journal entry. The data is stored in mood_journal.json.
- **View Trends**: Click "Show Mood Trends" to display a graphical representation of your mood history (pending implementation in the app).

3. JSON Structure:
The entries are stored in a JSON file (mood_journal.json) in the following format:

```json
[
    {
        "date": "2023-09-01",
        "time": "14:35:22",
        "mood": "Happy",
        "entry": "Today was a good day!"
    },
    {
        "date": "2023-09-02",
        "time": "10:15:03",
        "mood": "Stressed",
        "entry": "A bit overwhelming, but managed."
    }
]
```

## Future Improvements

### Graphical Mood Trends: 
Implement a graphical feature to show trends over weeks or months.

### UI Enhancements: 
Improve the appearance of the UI with better color schemes and font choices.

## Contributing
Feel free to fork this project, submit pull requests, or open issues to suggest improvements or report bugs.