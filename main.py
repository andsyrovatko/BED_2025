import sys
import os
from text_restorer import TextRestorer

# sys - for sys parameters use as sys;
# os  - for file access and manipulate with them;
# TextRestorer - import this class from text_restorer.py

def main():
    # Path to vocabulary (check that 'words_alpha.txt' exist in . (the same dir) or use full path below.
    vocabulary_path = os.path.join(os.path.dirname(__file__), 'words_alpha.txt')

    # Create or use existed file 'input_corrupted_text.txt' for destroyed input text for next recovering. Init output recovered text file.
    input_text_filename = "input_corrupted_text.txt"
    output_filename = "recovered_text.txt"

    print("--- Програма для відновлення тексту ---")
    print("\n[🚀] Завантажуємо словник...")
    restorer = TextRestorer(vocabulary_path)
    print("[✅] Словник завантажено.")

    # Read corrupted text
    corrupted_text = ""
