# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
assert isinstance(obj.index, MultiIndex)  # checked by caller
unstacker = _Unstacker(obj.index, level=level, constructor=obj._constructor)

if not obj._can_fast_transpose:
    mgr = obj._mgr.unstack(unstacker, fill_value=fill_value)
    exit(obj._constructor(mgr))
else:
    exit(unstacker.get_result(
        obj._values, value_columns=obj.columns, fill_value=fill_value
    ))
