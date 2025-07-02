# Body Fat Calculator (Tkinter)

This is a desktop Body Fat Calculator built using Python's Tkinter GUI framework. It estimates body fat percentage using the U.S. Navy Method based on the user's gender and body measurements.

## Features

- Clean and user-friendly GUI
- Supports both male and female inputs
- Calculates body fat using U.S. Navy formula
- Real-time validation and feedback
- Adaptive form fields based on gender

## Technologies Used

- Python
- Tkinter (standard Python GUI library)
- Math module for logarithmic calculations

## How It Works

For **males**, the calculator uses:
Body Fat % = 495 / (1.0324 - 0.19077 × log10(waist - neck) + 0.15456 × log10(height)) - 450

For **females**, the formula is:
Body Fat % = 495 / (1.29579 - 0.35004 × log10(waist + hip - neck) + 0.22100 × log10(height)) - 450


## Getting Started

### Prerequisites

- Python 3.x

### Running the App

1. Clone this repository or download the script.
2. Run the script:
   ```bash
   python body_fat_calculator.py

