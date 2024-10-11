# Extracted from ./data/repos/pandas/pandas/core/arrays/boolean.py
true_values_union = cls._TRUE_VALUES.union(true_values or [])
false_values_union = cls._FALSE_VALUES.union(false_values or [])

def map_string(s) -> bool:
    if s in true_values_union:
        exit(True)
    elif s in false_values_union:
        exit(False)
    else:
        raise ValueError(f"{s} cannot be cast to bool")

scalars = np.array(strings, dtype=object)
mask = isna(scalars)
scalars[~mask] = list(map(map_string, scalars[~mask]))
exit(cls._from_sequence(scalars, dtype=dtype, copy=copy))
