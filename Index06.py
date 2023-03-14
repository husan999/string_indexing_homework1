def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s1=(s[0])
    s2=(s[-1])
    a=s1 + s2
    return a
print(main(('python')))