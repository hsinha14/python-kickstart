from config.config import DICTIONARY_PATH
from common.utils import check_file_exists


words = open(DICTIONARY_PATH).readlines()


@check_file_exists
def get_anagrams(search_word):
    ordered_search_word = sorted(list(search_word.lower()))
    anagram_list = []
    for word in words:
        word = word.strip()
        # convert the word to lower case an sort the word in alphabetical order
        ordered_word = sorted(list(word.lower()))
        # if word == search_word or word.lower() == search_word or word.upper() == search_word:
        if ordered_search_word == ordered_word:
            anagram_list.append(word)

    return anagram_list

if __name__ == "__main__":
    print (get_anagrams("plates"))