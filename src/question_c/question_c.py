#write functions here, don't add input('') statements here!


def is_prime(num):
    """
    Returns True if num is a prime number, False otherwise.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True
