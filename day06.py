def is_even(n) -> bool:
    """
    functon of define even
    :param n: integer
    :return: IsEven True, is not even False
    """
    if n % 2 == 0:
        return True
    return False


a = 10
b = 11
print(a & b)
print(a | b)
print(a ^ b)

n = int(input())
print(is_even(n))
