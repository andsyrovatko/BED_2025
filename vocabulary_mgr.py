import collections

# collections - for defaultdict use (to simple count N words);

### This part of the code belongs to the VocabularyManager class, which, as we discussed, is responsible for loading, storing, and managing data from a dictionary (vocabulary).

class VocabularyManager:
    def __init__(self, vocabulary_path):
        self.words = set()
        # Using collections for harder situation (use N-gram)
        self.letter_frequencies = collections.defaultdict(int)
        self.bigrams = collections.defaultdict(int) # Для N-грам (слово1, слово2) -> частота
        self._load_vocabulary(vocabulary_path)

    def _load_vocabulary(self, path):
        # Load words from dictionary (vocabulary) and calc frequency
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    word = line.strip().lower() # Set to lowcase
                    if word.isalpha(): # Check if these are letters
                        self.words.add(word)
                        # frequency letter calc (to change *)
                        for char in word:
                            self.letter_frequencies[char] += 1
                        # Calculation of bigrams (for evaluating word sequences) - later
        except FileNotFoundError:
            print(f"[❌] Помилка: файл словника '{path}' не знайдено.")
            print("Будь ласка, переконайтеся, що файл 'words_alpha.txt' знаходиться в тій же директорії, що й 'main.py' та 'dictionary_manager.py'.")
            print("Ви можете завантажити його, наприклад, з GitHub: https://github.com/dwyl/english-words/blob/master/words_alpha.txt")
            exit()
        except Exception as e:
            print(f"[❌] Помилка під час завантаження словника: {e}")
            exit()
