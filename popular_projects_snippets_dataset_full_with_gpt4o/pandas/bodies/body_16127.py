# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# dir contains string-like values of the Index.
s = Series(index=index, dtype=object)
dir_s = dir(s)
for i, x in enumerate(s.index.unique(level=0)):
    if i < 100:
        assert not isinstance(x, str) or not x.isidentifier() or x in dir_s
    else:
        assert x not in dir_s
