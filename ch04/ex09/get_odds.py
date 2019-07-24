def get_odds():
    return [number for number in range(10) if number % 2 == 1]


print(get_odds()[2])
