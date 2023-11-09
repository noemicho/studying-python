
def countVowels(string):
    totalChar = 0
    numVowels = 0
    for i in string:
        totalChar += 1
        if i in ' ':
            totalChar += -1
        if i in 'AaEeIiOoUu':
            numVowels += 1
    print('\n               ', numVowels, 'vowels','of', totalChar, 'characters\n' )
    return numVowels

def main():
    print('****** Counting how many VOWELS a string has *******\n \n')
    while True:
        string = input('Type your text: \n')
        countVowels(string)

main()