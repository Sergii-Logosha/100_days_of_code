# 25.11.2023 Sergii Logosha sergiilogosha@gmail.com

# Program outputs list of NATO accepted words for every letter in the word
# that user inputs

import pandas

nato_alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row['letter']: row['code'] for (index, row)
                      in nato_alphabet_df.iterrows()}

while True:
    user_input = input('Type in a word: ').upper()
    try:
        nato_alphabet_list = [nato_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print('Only letters alowed, try again')
    else:
        print(nato_alphabet_list)
        break
