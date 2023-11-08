"""AVERAGE"""


def main():
    print('********* CALCULATING AVERAGES *********\n \n')

    print('Type your list of numbers: \n')

    n = ''
    array = []
    
    while n!='end':
        n = input()
        array.append(n)
        
    if n=='end':
        array.remove(n)
        print('\n----end of the list----')

    print(array)
    
    
main()