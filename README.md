# Introduciton

> The aim of this project was to create a Hangman game, by using Python, where the player would input their guess. Technology used for this project was Python. 

## Milestone 1

- A simple function was made to ask the user for an input for the 1st Milestone. The function would then call the check_letter() function to check if the letter guessed is in the word.
  
```python
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
```

## Milestone 2

- In Milestone 2, the conecpt of Object Oriented Programming (OOP) was used to define the attributes for the game. The predefined attributes for the game were number of lives and the word list.

```python
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
```

## Milestone 3

- In Milestone 3, the check_letter() function was coded. The function was prgrammed to check the letter that the user had input and see if it mathced with any of the letters in the word that the user had to guess. If the letter matched, the function would replace the empty space with the correct letter whilst keeping the un-guessed letters blank. The function would also reduce the life by 1 if the user had uinput the incorrect letter, as well as, displaying the letters which have been guessed to help the user keep track of the letters they have guessed.

- This function is called by the ask_letter function
```python
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
```
## Milestone 4
- In the final milestone, all of the logic was tied together. The play_game function was created to iteratively ask the user for a letter until the user guessed the word or runs out of lives. 
```python
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
```
- To add the finihsing touch, I added the iconic hangman diagram that would show when the user had guessed an incorrect letter.

## Conclusions

- The was my 1st Python project, I learnt how attributes are defined and the basics of OOP.
