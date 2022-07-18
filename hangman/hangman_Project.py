'''
Hssnahmed53
'''
import random

hangman_hanged = [
"""   __________
     |       |
     |      (_)
     |      \|/
     |       |
     |       |
     |      / \\
     |
    _|___
    
        """,

"""   __________
     |       |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    
        """,

"""   __________
     |       |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
    
        """,
"""   __________
     |       |
     |      (_)
     |      
     |       
     |      
     |
    _|___
    
        """,
"""   __________
     |      |
     |      
     |      
     |       
     |      
     |
    _|___
    
        """
]

class Hangman:

    def __init__(self, word_list, num_lives=5):

        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_letters = []
        print(f'The mystery word has {len(self.word)} characters')
        print(self.word_guessed)

        pass

    def check_letter(self, letter) -> None:
                       
        if letter in self.word:
            for index, char in enumerate(self.word):
                if letter == char:
                    self.word_guessed[index] = letter
                    print(f'Brilliant! the letter {letter} is in the word')
                    self.num_letters -= 1
                    self.list_letters.append(letter) 
                    print(self.word_guessed)              
        else:
            self.num_lives -= 1
            self.list_letters.append(letter)
            print(f'Woops {letter} not in the word')
            print(hangman_hanged[self.num_lives])
            print(self.list_letters)
            print(f'Looks like you have {self.num_lives} left')
        pass

    def ask_letter(self):
          
        while True and self.num_lives > 0:
            letter = input(f'Enter a single character: ').lower()
            if len(letter) > 1:
                print(f'Please, enter just one character')
            elif letter.isalpha() is False:
                print(f'Only enter alphabets')    
            elif len(letter) == 1 and letter in self.list_letters:                                      
                    print(f'{letter} was already tried')          
            else:                         
                self.check_letter(letter)
                break   
        else:
            print(f'Please enter a character')
            print(letter)                                                                      
        pass

def play_game(word_list):
    
    game = Hangman(word_list, num_lives=5)

    while game.num_lives >= 0:
        if game.num_lives > 0 and '_' in game.word_guessed:
            game.ask_letter()
        elif '_' not in game.word_guessed:
            print(f'Congratulations, you won!')
            print(f'The word was','' .join(game.word))
            break
        elif game.num_lives == 0:
            print(f'You ran out of lives. The word was {game.word}')
            break
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
