# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
klass = listlike_box

idx = simple_index
if isinstance(idx, (DatetimeIndex, TimedeltaIndex)):
    # where does not preserve freq
    idx = idx._with_freq(None)

cond = [True] * len(idx)
result = idx.where(klass(cond))
expected = idx
tm.assert_index_equal(result, expected)

cond = [False] + [True] * len(idx[1:])
expected = Index([idx._na_value] + idx[1:].tolist(), dtype=idx.dtype)
result = idx.where(klass(cond))
tm.assert_index_equal(result, expected)
