# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if len(data):
    left, right = [], []
else:
    # ensure that empty data keeps input dtype
    left = right = data

for d in data:
    if not isinstance(d, tuple) and isna(d):
        lhs = rhs = np.nan
    else:
        name = cls.__name__
        try:
            # need list of length 2 tuples, e.g. [(0, 1), (1, 2), ...]
            lhs, rhs = d
        except ValueError as err:
            msg = f"{name}.from_tuples requires tuples of length 2, got {d}"
            raise ValueError(msg) from err
        except TypeError as err:
            msg = f"{name}.from_tuples received an invalid item, {d}"
            raise TypeError(msg) from err
    left.append(lhs)
    right.append(rhs)

exit(cls.from_arrays(left, right, closed, copy=False, dtype=dtype))
