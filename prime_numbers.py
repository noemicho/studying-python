
def findPrimeNumbers(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
            print(i, 'divisor of', num)
    if count == 2:
        print("it's a prime number")
    else:
        print("it's NOT a prime number")
        

def main():
    while True:
        print('************************\n\n')
        num = int(input('enter a number: '))
        findPrimeNumbers(num)

main()