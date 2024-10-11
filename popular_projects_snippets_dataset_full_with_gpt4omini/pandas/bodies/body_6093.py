# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
empty = data[:0]

result = empty.take([-1], allow_fill=True)
assert na_cmp(result[0], na_value)

msg = "cannot do a non-empty take from an empty axes|out of bounds"

with pytest.raises(IndexError, match=msg):
    empty.take([-1])

with pytest.raises(IndexError, match="cannot do a non-empty take"):
    empty.take([0, 1])
