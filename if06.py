def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    n=n//10
    x2=n%10
    n=n//10
    x3=n%10
    n=n//10
    x4=n%10
    n=n//10
    x5=n%10
    n=n//10

    max=x1
    idx=1
    if max<x2:
        max=x2
        idx=2
    if max<x3:
        max=x3
        idx=3
    if max<x4:
        max=x4
        idx=4
    if max<x5:
        max=x5
        idx=5

    return idx

print(main(76514))
