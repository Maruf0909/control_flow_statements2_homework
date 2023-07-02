def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    min=a
    if min>b:
        min=b
    if min>c:
        min=c

    return min
print(main(-1,-4,-2))