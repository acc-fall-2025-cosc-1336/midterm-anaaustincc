#write functions here, don't add input('') statements here!
def test_config():
    return True


def get_sum_of_evens(num):
    """
    Returns the sum of all even numbers from 2 up to and including num.
    Example: get_sum_of_evens(10) returns 30 (2+4+6+8+10)
    """
    return sum(i for i in range(2, num + 1, 2))