import random
import time

random.seed(time.time())


# roll_die returns a random number used to look up words in the wordlist.
# We 'virtually' roll a dice 5 times to generate the number to use.
def roll_dice():
    final_number = ''

    for roll in range(5):
        roll = randint(1, 6)
        final_number += str(roll)

    return final_number


# lookup_associated_word takes a combination of dice rolls and
# returns the associated word
def lookup_associated_word(dice_number):
    # 1. Read file
    with open("eff_large_wordlist.txt") as wordlist:
        pass
    # 2. Lookup word associated with dice_number
    # 3. Return word
    pass


# generate_diceware_password: Takes in a length representing
# the number of words that will compose the final passphrase
def generate_diceware_password(passphrase_length):
    passphrase_list = []
