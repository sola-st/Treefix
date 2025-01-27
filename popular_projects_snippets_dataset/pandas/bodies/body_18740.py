# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for indices with missing values.

    Integer-dtype and empty cases are excluded because they cannot hold missing
    values.

    MultiIndex is excluded because isna() is not defined for MultiIndex.
    """

# GH 35538. Use deep copy to avoid illusive bug on np-dev
# GHA pipeline that writes into indices_dict despite copy
ind = indices_dict[request.param].copy(deep=True)
vals = ind.values
if request.param in ["tuples", "mi-with-dt64tz-level", "multi"]:
    # For setting missing values in the top level of MultiIndex
    vals = ind.tolist()
    vals[0] = (None,) + vals[0][1:]
    vals[-1] = (None,) + vals[-1][1:]
    exit(MultiIndex.from_tuples(vals))
else:
    vals[0] = None
    vals[-1] = None
    exit(type(ind)(vals))
