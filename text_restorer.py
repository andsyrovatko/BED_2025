import difflib
from vocabulary_mgr import VocabularyManager

class TextRestorer:
    def __init__(self, vocabulary_path):
        self.vocabulary_mgr = VocabularyManager(vocabulary_path)
        self.most_frequent_letters = self.vocabulary_mgr.get_most_frequent_letters()

    # Main text restore function.
    def restore_text(self, corrupted_text):
        corrupted_text = corrupted_text.lower()
        recovered_words = []
        segments = corrupted_text.split('*')
        segments = [seg for seg in segments if seg]

        for seg in segments:
            # For long segments, perform an in-depth search
            if len(seg) > 15:
                words_in_seg = self._restore_from_long_segment(seg)
                recovered_words.extend(words_in_seg)
            else:
                found_words = self._find_possible_words(seg)
                if found_words:
                    best_word = max(found_words, key=self._score_word_by_letter_frequency)
                    recovered_words.append(best_word)
                else:
                    # If the word is not found, add the original
                    recovered_words.append(seg)

        return " ".join(recovered_words)

    def _restore_from_long_segment(self, segment):
        recovered_parts = []
        pos = 0
        length = len(segment)

        previous_word = None

        while pos < length:
            best_word = None
            best_len = 0
            best_score = -1
            max_len = min(20, length - pos)

            for l in range(max_len, 0, -1):
                subseg = segment[pos:pos + l]
                candidates = self._find_possible_words(subseg)

                # If there are no exact words, try a fuzzy search
                if not candidates:
                    candidates = self._find_fuzzy_words(subseg, max_dist=2)

                for word in candidates:
                    score = self._score_word_by_letter_frequency(word)
                    if previous_word:
                        bigram_score = self.vocabulary_mgr.get_bigram_frequency(previous_word, word)
                        if bigram_score > 0:
                            score += 2000 * (bigram_score / (1 + len(word)))
                        else:
                            score -= 100

                    if self.vocabulary_mgr.is_word(word):
                        score += 500
                    else:
                        score -= 1000

                    if score > best_score:
                        best_word = word
                        best_score = score
                        best_len = l

                if best_word and best_len > 1:
                    break

            if best_word:
                recovered_parts.append(best_word)
                previous_word = best_word
                pos += best_len
            else:
                # If the word is not found, skip 1 character
                pos += 1

        return recovered_parts

    def _score_word_by_letter_frequency(self, word):
        return sum(self.vocabulary_mgr.letter_frequencies.get(c, 0) for c in word)

    def _find_possible_words(self, segment):
        possible_words = []
        segment_len = len(segment)

        candidate_words_by_length = self.vocabulary_mgr.get_words_by_length(segment_len)

        for dict_word in candidate_words_by_length:
            is_match = True
            for i, char_in_segment in enumerate(segment):
                if char_in_segment != dict_word[i]:
                    is_match = False
                    break
            if is_match:
                possible_words.append(dict_word)

        if possible_words:
            print(f"[DEBUG] Для сегмента '{segment}' знайдено слова: {possible_words[:5]} ...")
        else:
            print(f"[DEBUG] Для сегмента '{segment}' не знайдено слів")

        return possible_words

    def _find_fuzzy_words(self, segment, max_dist=2):
        length = len(segment)
        candidates = []
        # Let's take words of length length-1, length, length+1
        for length_diff in range(-1, 2):
            words_of_length = self.vocabulary_mgr.get_words_by_length(length + length_diff)
            candidates.extend(words_of_length)

        close_words = []
        for word in candidates:
            dist = self._levenshtein_distance(segment, word)
            if dist <= max_dist:
                close_words.append(word)

        if close_words:
            print(f"[DEBUG] Для сегмента '{segment}' знайдено fuzzy-слова: {close_words[:5]} ...")
        else:
            print(f"[DEBUG] Для сегмента '{segment}' fuzzy-слова не знайдено")

        return close_words

    def _levenshtein_distance(self, a, b):
        if len(a) < len(b):
            return self._levenshtein_distance(b, a)
        if len(b) == 0:
            return len(a)
        previous_row = range(len(b) + 1)
        for i, c1 in enumerate(a):
            current_row = [i + 1]
            for j, c2 in enumerate(b):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]
