from letter_state import LetterState

class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    
    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def gameWin(self): # check if player wins
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret # if still have attempts and the last guessed word is correct
    
    def remainingAttempts(self): # return integer
        return self.MAX_ATTEMPTS - len(self.attempts)
    
    def stillAttempt(self): # return boolean
        return self.remainingAttempts() > 0 and not self.gameWin()
    
    def guess(self, word:str):
        word = word.upper()

        # Convert a copy of secret to a list
        remaining_secret = list(self.secret)

        # Initalize the results array
        result = []
        for char in word:
            result.append(LetterState(char))

        # check for GREEN letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.in_right_position = True
                remaining_secret[i] = '*'

        # check for YELLOW letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]

            # Skip letter if it is already in the right place
            if letter.in_right_position:
                continue

            # Otherwise, check if the letter is in the word, and void that index
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = '*'
                    letter.in_word = True
                    break
        
        return result