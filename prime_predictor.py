import sys

# Simple function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num  0 == 0:
            return False
    return True

# Main function to take input and predict
if __name__ == '__main__':
    number = int(sys.argv[1])
    if is_prime(number):
        print(f'{number} is a prime number.')
    else:
        print(f'{number} is not a prime number.')