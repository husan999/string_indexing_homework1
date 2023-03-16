def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x1=int(s)//10000
    x2=int(s)//1000%10
    x3=int(s)//100%10
    x4=int(s)//10%10
    x5=int(s)%10
    x=x1+x2+x3+x4+x5
    return x
print(main("12332"))