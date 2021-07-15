number = int(input('Enter a number from 1 to 10: '))

if number == 1:
    roman = 'I'
elif number == 2:
    roman = 'II'
elif number == 3:
    roman = 'III'
elif number == 4:
    roman = 'IV'
elif number == 5:
    roman = 'V'
elif number == 6:
    roman = 'VI'
elif number == 7:
    roman = 'VII'
elif number == 8:
    roman = 'VIII'
elif number == 9:
    roman = 'IX'
elif number == 10:
    roman = 'X'

if number >= 1 and number <= 10:
    print('The number', number, 'is equal to', roman, 'in roman number.')
else:
    print('Invalid number, you must enter a number between 1 and 10.')
