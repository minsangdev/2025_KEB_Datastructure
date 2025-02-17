def is_even(n) -> bool:
    """
    functon of define even
    :param n: integer
    :return: IsEven True, is not even False
    """
    return not n & 1


n = int(input())
print(is_even(n))
