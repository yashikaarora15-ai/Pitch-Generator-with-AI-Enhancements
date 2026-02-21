import csv
import os
from datetime import datetime

# Ensure data folder exists
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

FILE_PATH = os.path.join(DATA_DIR, "ratings.csv")

def save_review(pitch, rating, ai_used):

    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow(["timestamp", "pitch", "rating", "ai_used"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            pitch,
            rating,
            ai_used
        ])