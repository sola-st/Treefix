# Extracted from ./data/repos/pandas/pandas/util/_validators.py
"""
    Checks whether 'kwargs' contains any keys that are not
    in 'compat_args' and raises a TypeError if there is one.
    """
# set(dict) --> set of the dictionary's keys
diff = set(kwargs) - set(compat_args)

if diff:
    bad_arg = list(diff)[0]
    raise TypeError(f"{fname}() got an unexpected keyword argument '{bad_arg}'")
