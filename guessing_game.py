import random

class WordGuessingGame:
    def __init__(self, words, max_attempts=12):
        """Initialize the game with list of word and max number of attempts"""
        self.words = words
        self.max_attempts = max_attempts
        self.word_to_guess = random.choice(self.words)
        self.guesses = '' # tracks all guessed characters
        self.attempts_left = self.max_attempts

    def display_word(self):
        display = ''
        for char in self.word_to_guess:
            if char in self.guesses:
                display += char + ''
            else:
                display += '_' # underscore for hidden letters
        print(display.strip())

    def guess_letter(self, letter):
        """Update guesses and reduces attempts if guess is wrong   """
        if letter in self.guesses:
            print("You already guess the letter!")
        else:
            self.guesses += letter
            if letter not in self.word_to_guess:
                self.attempts_left -= 1
                print(f"Wrong guess ! attempts left {self.attempts_left}")
            else:
                print("Good guess!")

    def check_win(self):
        """check if the player has guessed the entire word  """
        for char in self.word_to_guess:
            if char not in self.guesses:
                return False
        return True

    def play_game(self):
        """Main game loop"""
        print("\nWelcome to word guessing game!")
        print(f"You have {self.max_attempts} attempts to guess the word")

        while self.attempts_left > 0:
            self.display_word()
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter! ")
                continue

            self.guess_letter(guess)

            if self.check_win():
                print(f"Congratulation! You guessed the word: {self.word_to_guess} ")
                break
        else:
            print(f"Game over ! The word was: {self.word_to_guess} ")

# Driver code
if __name__ == '__main__':
    word_list =  ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player',
                  'condition', 'reverse', 'water', 'board', 'geeks']
    game = WordGuessingGame(word_list)
    game.play_game()


# Reference: https://www.geeksforgeeks.org/python-program-for-word-guessing-game/