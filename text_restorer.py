from vocabulary_mgr import VocabularyManager

class TextRestorer:
    def __init__(self, vocabulary_path):
        self.vocabulary_mgr = VocabularyManager(vocabulary_path)
        self.most_frequent_letters = self.dictionary_manager.get_most_frequent_letters()

    # Main text restore function.
    def restore_text(self, corrupted_text):
        corrupted_text = corrupted_text.lower() # Se to lower_case

        # Search the longest word
        recovered_parts = []
        current_pos = 0
        text_length = len(corrupted_text)

        while current_pos < text_length:
            best_word = None
            best_word_len = 0

            # Limit the length to avoid excessive calculations
            max_search_length = min(20, text_length - current_pos + 1)

            # Trying to find a word by going through the possible lengths from longest to shortest to find the best match.
            for length in range(max_search_length, 0, -1):
                segment = corrupted_text[current_pos : current_pos + length]

                # Looking for direct matches or with asterisks.
                found_words = self._find_possible_words(segment)

                if found_words:
                    # For simplicity, we will take the first word found (in future should be an N-gram-based selection).
                    best_word = found_words[0]
                    best_word_len = len(best_word)
                    break # Found the longest word, let's move on

            if best_word:
                recovered_parts.append(best_word)
                current_pos += best_word_len
            else:
                # If the word is not found, it may be an error or a very corrupted fragment.
                recovered_parts.append(corrupted_text[current_pos])
                current_pos += 1

        return " ".join(recovered_parts)

#    def _find_possible_words(self, segment):

