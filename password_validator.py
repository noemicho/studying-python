
def checker(string):
    
    if len(string) < 8 :
        print('\n                                  TOO WEAK')
        print('\nPassword must have at least 8 characters...')
    else:   
        num_char = 0
        upper = 0
        lower = 0
        number = 0
        special = 0
        for i in string:
            num_char += 1
            if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                upper += 1
            if i in 'abcdefghijklmnopqrstuvwxyz':
                lower += 1
            if i in '0123456789':
                number += 1
            if i in '@#$%&*_-.':
                special += 1
        if upper < 2 or lower == 0:
            print('\n                                  WEAK')
            print('\nPassword could have at least 2 uppercase and 1 lowercase letter')
        elif number == 0:
            print('\n                                  FAIR')
            print('\nPassword could have numbers...')
        elif special == 0:
            print('\n                                  STRONG')
            print('\nPassword could special characters...')
        else:
            print('\n                                  VERY STRONG')

def main():
    while True:
        print('WELCOME TO PASSWORD VALIDATOR\n\n')
        p = input('Type your password: ')
        checker(p)
        print('\n________________________________________\n')

main()