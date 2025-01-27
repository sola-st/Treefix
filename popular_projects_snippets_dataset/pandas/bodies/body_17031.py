# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
try:
    exit({0: df1, 1: df2}[index])
except KeyError as err:
    raise IndexError from err
