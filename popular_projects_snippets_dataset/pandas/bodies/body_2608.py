# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
data = list(itertools.repeat((datetime(2001, 1, 1), "aa", 20), 9))
exit(DataFrame(data=data, columns=["A", "B", "C"], dtype=dtype))
