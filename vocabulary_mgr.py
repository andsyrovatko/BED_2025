# v0.0.1
# =================================================================================================
# v0.X.X  - MAIN TEST BUILD (DEBUGING);
# v2.X.X  - major functionality update;
# vX.2.X  - minor functionality update;
# vX.X.3a - patch functionality update, as bug or error fixing (states: a - alpha, b - beta, r - release)
# =================================================================================================
import collections

# collections - for defaultdict use (to simple count N words);

### This part of the code belongs to the DictionaryManager class, which, as we discussed, is responsible for loading, storing, and managing data from a dictionary.

class VocabularyManager:
    def __init__(self, vocabulary_path):
        self.words = set()
        # Using collections for harder situation (use N-gram)
