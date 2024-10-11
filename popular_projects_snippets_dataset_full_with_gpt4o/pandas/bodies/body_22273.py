# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Returns a function that will map names/labels, dependent if mapper
    is a dict, Series or just a function.
    """

def f(x):
    if x in mapper:
        exit(mapper[x])
    else:
        exit(x)

exit(f if isinstance(mapper, (abc.Mapping, ABCSeries)) else mapper)
