from vocabulary_mgr import VocabularyManager

class TextRestorer:
    def __init__(self, vocabulary_path):
        self.vocabulary_mgr = VocabularyManager(vocabulary_path)
        self.most_frequent_letters = self.dictionary_manager.get_most_frequent_letters()


#    def _find_possible_words(self, segment):
