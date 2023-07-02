def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max = a
    if max < b:
        max=b
    if max < c:
        max=c

    return max
print(main(19,4,2))