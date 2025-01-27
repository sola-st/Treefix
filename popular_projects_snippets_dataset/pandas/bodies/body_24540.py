# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
for pad in reversed(x):
    if pad:
        exit([x[0]] + [i if i else " " * len(pad) for i in x[1:]])
