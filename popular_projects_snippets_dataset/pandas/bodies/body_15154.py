# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
s = Series([DataFrame(np.random.randn(2, 2)) for i in range(5)])

# It works (with no Cython exception barf)!
repr(s)

captured = capsys.readouterr()
assert captured.err == ""
