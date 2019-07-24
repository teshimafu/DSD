
def amount_compare(guess_me):
    if guess_me < 7:
        return 'too low'
    elif guess_me == 7:
        return 'just right'
    elif guess_me > 7:
        return 'too high'


guess_me = 7

print(amount_compare(guess_me))
