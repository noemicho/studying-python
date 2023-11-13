
def binary_search(listN, num):
    
    array = list(map(int, listN.split()))
    arraySorted = sorted(array)
    right = 0
    left = len(arraySorted) - 1
    print('Sorted Array:', arraySorted)
 
    while right <= left:
        middle = (right + left)//2
        if arraySorted[middle] == num:
            return middle
        elif arraySorted[middle] > num:
            left = middle - 1 
        elif arraySorted[middle] < num:
            right = middle + 1
    
    return -1



def main():
    print('*********BINARY SEARCH*********\n \n')

    listN = input('Enter your list of numbers: ')
    num = int(input('TARGET? '))
    result = binary_search(listN, num)
    print('Index:', result)
    if result == -1:
        print('Not found')

main()