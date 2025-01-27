# Extracted from https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats
def sq(n):
    """
    Return the square of n. 
    """
    return n * n

def sq(n):
    """Returns the square of n."""
    return n * n

def sq(n):
    """
    Return the square of n, accepting all numeric types:

    >>> sq(10)
    100

    >>> sq(10.434)
    108.86835599999999

    Raises a TypeError when input is invalid:

    >>> sq(4*'435')
    Traceback (most recent call last):
      ...
    TypeError: can't multiply sequence by non-int of type 'str'

    """
    return n*n

def sq(n):
    """Return the squared result. 
    ...

