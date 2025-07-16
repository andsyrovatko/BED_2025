# v0.0.5
# =================================================================================================
# v0.X.X  - MAIN TEST BUILD (DEBUGING);
# v2.X.X  - major functionality update;
# vX.2.X  - minor functionality update;
# vX.X.3a - patch functionality update, as bug or error fixing (states: a - alpha, b - beta, r - release)
# =================================================================================================
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

    # Read corrupted text (from file)
    corrupted_text = ""
    try:
        with open(input_text_filename, 'r', encoding='utf-8') as f:
            corrupted_text = f.read().strip()
        print(f"\n[📄] Вхідний текст успішно зчитано з файлу '{input_text_filename}'")
        print(f"Пошкоджений текст (перші 100 символів): {corrupted_text[:100]}...")
    except FileNotFoundError:
        print(f"[❌] Помилка: Вхідний файл '{input_text_filename}' не знайдено.")
        print(f"Будь ласка, створіть файл '{input_text_filename}' у тій же директорії та вставте туди пошкоджений текст.")
        sys.exit(1) # EXIT 1 (if there is no file))
    except Exception as e:
        print(f"[❌] Помилка під час зчитування вхідного файлу: {e}")
        sys.exit(1) # EXIT 1 (if there is trouble to read file)

