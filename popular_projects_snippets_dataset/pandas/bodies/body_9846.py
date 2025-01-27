# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
if len(args) < 2:
    raise ValueError("The function needs two arguments")
array, scale = args
exit(array.sum() / scale)
