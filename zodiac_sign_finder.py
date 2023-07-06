birthYear = int(input('Enter your birth year: '))
last_digits = birthYear % 10

if last_digits == 0 or last_digits == 1:
    print('Your Zodiac element : Metal ')
elif last_digits == 2 or last_digits == 3:
    print('Your Zodiac element : Water ')
elif last_digits == 4 or last_digits == 5:
    print('Your Zodiac element : Wood ')
elif last_digits == 6 or last_digits == 7:
    print('Your Zodiac element : Fire ')
elif last_digits == 8 or last_digits == 9:
    print('You Zodiac element : Earth ')