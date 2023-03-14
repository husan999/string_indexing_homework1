def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s1=int(s[0])
    s2=int(s[-2])
    a=int(s1 + s2)
    return a
print(main(('12340')))