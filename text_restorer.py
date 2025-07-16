from vocabulary_mgr import VocabularyManager

class TextRestorer:
    def __init__(self, vocabulary_path):
        self.vocabulary_mgr = VocabularyManager(vocabulary_path)
        self.most_frequent_letters = self.vocabulary_mgr.get_most_frequent_letters()

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

        # Recover string using 'space' as separate
        return " ".join(recovered_parts)

    # Function to find all posible words
    def _find_possible_words(self, segment):
        possible_words = []
        segment_len = len(segment)

        # Get all words from a dictionary of a given length
        candidate_words_by_length = self.vocabulary_mgr.get_words_by_length(segment_len)

        known_chars_in_segment = [c for c in segment if c != '*']
        unknown_char_count = segment.count('*')

        for dict_word in candidate_words_by_length:
            # Check for a direct match with '*'
            is_match = True
            for i, char_in_segment in enumerate(segment):
                if char_in_segment != '*' and char_in_segment != dict_word[i]:
                    is_match = False
                    break
            if is_match:
                possible_words.append(dict_word)

        if unknown_char_count > 0 or len(known_chars_in_segment) > 0:
            pass # N-gramm update (for the future)

        # Return the found words or the original segment
        return possible_words if possible_words else [segment]
