""" This script gets pairs of prime numbers that when added together result in an even number """
def get_prime_pairs(number):
    """gets pairs of prime numbers that when added together result in an even number"""
    list_num1_primes = []
    list_prime_num1_num2_pairs = []
    if number % 2 == 1: # Break if number is odd
        return False
    for num1 in range(2, number): # check if num1 is a prime
        num1_is_prime = True
        divisor = 2
        while divisor < num1:
            if num1 % divisor == 0:
                num1_is_prime = False
            divisor += 1
        if num1_is_prime:
            list_num1_primes.append(num1)
            # check if num2 = number - num1 is prime
            num2 = number - num1
            if num2 >= 2:
                num2_is_prime = True
                divisor = 2
                while divisor < num2:
                    if num2 % divisor == 0:
                        num2_is_prime = False
                    divisor += 1
                # Prints if num1 and num2 are prime and don't repeat pairs numbers
                if num2_is_prime and num2 not in list_num1_primes: # if num2 was not printed as num1
                    list_prime_num1_num2_pairs.append((num1, num2))
    return list_prime_num1_num2_pairs


def print_prime_pairs(number, pairs_to_print):
    """print the resulting pairs of numbers"""
    for num1, num2 in pairs_to_print:
        print(f"The number {number} equals to the sum of {num1} and {num2}")


def main():
    """ Prompts the user for an even number .
        Get prime pairs.
        Print list of prime pairs.

    """
    print("Get pairs of prime numbers that when added together result in an even number")
    while True:
        try:
            input_number = int(input("\nEnter an even number to find its prime pairs: "))
            pairs_list = get_prime_pairs(input_number)
            print_prime_pairs(input_number, pairs_list)
            break
        except ValueError as error:
            print(f"ERROR: You did NOT enter a number.\n{error}")
        except TypeError:
            print(f"ERROR: You did NOT enter an even number.")

if __name__ == '__main__':
    main()