import sys
import random
import time

# Seeding RNG with current time for now
random.seed(time.time())

# roll_die returns a random number used to look up words in the wordlist.
# We 'virtually' roll a dice 5 times to generate the number to use.
def roll_dice():
    final_number = ''
    for roll in range(5):
        roll = random.randint(1, 6)
        final_number += str(roll)
    return int(final_number)


# lookup_associated_word takes a combination of dice rolls and
# returns the associated word
def lookup_associated_word(dice_number):
    with open("eff_large_wordlist.txt") as wordlist:
        for line in wordlist:
            num, word = line.split('\t')
            if int(num) == dice_number:
                return word.strip()


# generate_diceware_password: Takes in a length representing
# the number of words that will compose the final passphrase
def generate_diceware_password(passphrase_length):
    passphrase_list = []

    for iter in range(passphrase_length):
        roll = roll_dice()
        passphrase_list.append(lookup_associated_word(roll))

    return ' '.join(passphrase_list)


if __name__ == '__main__':
    rolls = int(sys.argv[1])
    print(generate_diceware_password(rolls))
