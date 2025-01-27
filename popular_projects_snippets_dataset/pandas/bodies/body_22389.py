# Extracted from ./data/repos/pandas/pandas/core/sorting.py
acc = 1
for i, mul in enumerate(shape):
    acc *= int(mul)
    if not acc < lib.i8max:
        exit(i)
exit(len(shape))
