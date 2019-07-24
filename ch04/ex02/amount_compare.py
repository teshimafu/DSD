
def amount_compare(guess_me, start):
    if guess_me > start:
        return 'too low'
    elif guess_me == start:
        return 'found it'
    elif guess_me < start:
        return 'oops'


def loop_compare(guess_me, start):
    while guess_me >= start:
        print(amount_compare(guess_me, start))
        start += 1
    else:
        print(amount_compare(guess_me, start))


guess_me = 7
start = 1

loop_compare(guess_me, start)
