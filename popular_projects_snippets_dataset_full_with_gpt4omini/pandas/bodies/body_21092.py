# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/scipy_sparse.py
whole = set(whole)
parts = [set(x) for x in parts]
if set.intersection(*parts) != set():
    raise ValueError("Is not a partition because intersection is not null.")
if set.union(*parts) != whole:
    raise ValueError("Is not a partition because union is not the whole.")
