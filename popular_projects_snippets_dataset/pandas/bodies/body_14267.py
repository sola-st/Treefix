# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_printing.py
data = [["a", "b", "c"], ["dd", "ee", "ff"], ["ggg", "hhh", "iii"]]
expected = "a  dd  ggg\nb  ee  hhh\nc  ff  iii"

adjoined = printing.adjoin(2, *data)

assert adjoined == expected
