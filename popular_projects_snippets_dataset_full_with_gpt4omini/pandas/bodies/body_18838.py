# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
if isinstance(x, Index):
    # return Index as it is to include values in the error message
    exit(x)

exit(type(x).__name__)
