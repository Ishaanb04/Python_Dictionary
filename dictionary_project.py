import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))

def define_word(word):
    if word in data:
        return data[word]
    else:
        new_word = get_close_matches(word, data.keys())
        if len(new_word) > 0:
            print(f'Did you mean {new_word[0]}')
            correct_word = str(input('Press Y or N: ')).lower()
            if correct_word == 'y':
                return data[new_word[0]]
            elif correct_word == 'n':
                the_word = str(input('Please enter the word again: ')).lower()
                return define_word(the_word)
            else:
                return 'Wrong input!'
        else:
            return 'No Word Found'

def print_word(word):
    if type(meaning) is list:
        for defn in meaning:
            print(f'=>{defn}')
    else:
        print(meaning)

user_input = str(input('Please enter a word to search in the dictionary: ')).lower()
meaning = define_word(user_input)
print_word(meaning)



