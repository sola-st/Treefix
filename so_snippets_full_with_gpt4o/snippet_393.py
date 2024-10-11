# Extracted from https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
line = filter(lambda char: char not in " ?.!/;:", line)

help(filter)
Help on built-in function filter in module __builtin__:

filter(...)
    filter(function or None, sequence) -> list, tuple, or string

    Return those items of sequence for which function(item) is true.  If
    function is None, return the items that are true.  If sequence is a tuple
    or string, return the same type, else return a list.

