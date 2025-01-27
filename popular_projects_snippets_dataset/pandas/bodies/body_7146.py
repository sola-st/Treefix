# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH 29539
dtype = invalid_dtype
msg = rf"Incorrect `dtype` passed: expected \w+(?: \w+)?, received {dtype}"
with pytest.raises(ValueError, match=msg):
    self._index_cls([1, 2, 3], dtype=dtype)
