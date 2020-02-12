# Step 1 - 3 in setup method, only runs once.
# Step 4 - 6 are part of the while loop. 

# Step 1 Make a list of words
# Step 2 Select randomly from the list, assign to secret
# Step 3 Create userview, a string of underscores equal in length to secret.
# 3.1 chances = 8
# Step 4 Print chances, userview in formatted string. 
# Step 5 Prompt for user input. Letters A-Z. Use .upper() or .lower(). 
# if guess.lower() in 'abcdefghijklmnopqrstuvwxyz':
#    Run a method to check if it's right, print the new word, remaining guesses, etc.
#    if guess.lower() in secret:
#        0: 'Good Guess!'
#        1: Get all indices of that letter, store in list
#        2: Replace matching indices in userview with that letter
#        3: Print new userview here, or at the beginning of each turn?
#    else:
#        1: 'Wrong!'
#        2: chances -= 1
#        3: f"You have {chances} left before you die."
#        
# else:
#     Print an error, ask for a-z

# Step 6: Below function/method to run after every turn
# if userview == secret:
#     'You Win!'
#     return True
# elif chances <= 0:
#     'You ran out of guesses and you DEEEEEAAAAADDD'
#      return True

#Put game in a while loop:
#   while active:
# Once the above function makes active False, the loop will end

import random
from IPython.display import clear_output

#Create the Object/Class for Hangman
class Hangman():
    
    def __init__(self, words = [
            'bargain', #This is a default parameter, a different list can be
            #passed when the class is instantiated
            'perfection',
            'plasma',
            'beautify',
            'notebook',
            'skydiving',
            'transcend',
            'salary',
            'burrito',
            'lentils'
        ]):
        self.words = words
        self.chances = 8
        self.secret = ''
        self.userview = ''
        self.pastguess = ''
        
    def setup(self):
        self.secret = self.words[random.randint(0,len(self.words)-1)]
        self.userview = '' #What the user will see in the console
        self.pastguess = '' #Ensures that the user isn't penalized for 
        # guessing same letters
        for x in range(len(self.secret)):
            self.userview += '_'
            
    def status(self):
        print(f"You have {self.chances} chances left. \n {self.userview}")
        
    def prompt(self):
        guess = input('Guess a letter! ').lower()
        if guess in 'abcdefghijklmnopqrstuvwxyz' and guess \
not in self.pastguess:
            self.pastguess += guess
            if guess in self.secret:
                print('\nGood Guess!')
     #  1: Get all indices of that letter, store in list
                indices = []
                for i, char in enumerate(self.secret):
                    if guess == char:
                        indices.append(i)
       #2: Replace matching indices in userview with that letter
                viewlist = [char for char in self.userview]
                #strings are immutable, so I casted userview as a list
                for i in indices: 
                    viewlist[i] = guess
                self.userview = ''.join(viewlist)
                if self.userview == self.secret:
                    "\nYou win!"
                    return True
            else:
                print('\nWrong!')
                self.chances -= 1
                if self.chances <= 0:
                    print('\nYou lose!')
                    return True
        else:
            print("\nYou need to choose a letter (a-z) you haven't chosen yet.")

    
def main():
    game = Hangman()
    active = True
    game.setup() #Step 1-3
    while active:
        game.status() # Step 4
        if game.prompt(): # Step 5
            active = False
    print(f"The word to guess was {game.secret}.")
    print("Thanks for playing!")

main()
