"""AVERAGE"""

def calculateAv(list):
    sum = 0
    for x in range(len(list)):
        item = list[x]
        sum = sum + item
    print('\nSum: ', sum)
    div = len(list)
    result = sum/div
    print('\n******* Average: ', '%.2f' % result, '*******\n')
    return result

def main():
    print('********* CALCULATING AVERAGES *********\n \n')

    while True:
        num = int(input('How many numbers? '))
        n = ''
        array = []
        print('\n')
        for i in range(num):
            n = float(input('Type the number: '))
            array.append(n)
        
        print('\nYour list: ', array)
        calculateAv(array)
    
main()