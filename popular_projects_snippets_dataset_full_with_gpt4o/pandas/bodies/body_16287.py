# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 19342
# test that construction of a Series with an index of different length
# raises an error
msg = r"Length of values \(3\) does not match length of index \(4\)"
with pytest.raises(ValueError, match=msg):
    Series(input, index=np.arange(4))
