import csv
import os
from datetime import datetime

FILE_PATH = "data/ratings.csv"

def save_review(pitch, rating, ai_used):
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "pitch_length", "rating", "ai_enhanced"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            len(pitch.split()),
            rating,
            ai_used
        ])