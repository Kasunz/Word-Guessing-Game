import random

class WordGuessingGame:
    def __int__(self, words, max_attempts=7):
        """Initialize the game with list of word and max number of attempts"""
        self.words = words
        self.max_attempts = max_attempts
        self.word_to_guess = random.choice(self.words)
        self.guesses = '' # tracks all guessed characters
        self.attempts_left = self.max_attempts




# Driver code
if __name__ == '__main__':
    word_list =  ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player',
                  'condition', 'reverse', 'water', 'board', 'geeks']