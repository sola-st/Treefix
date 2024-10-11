# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
dates = date_range("01-Jan-2013", periods=12, freq="MS")
ts = Series(np.random.randn(12), index=dates)

# GH3035
# index.map is used to apply grouper to the index
# if it fails on the elements, map tries it on the entire index as
# a sequence. That can yield invalid results that cause trouble
# down the line.
# the surprise comes from using key[0:6] rather than str(key)[0:6]
# when the elements are Timestamp.
# the result is Index[0:6], very confusing.

msg = r"Grouper result violates len\(labels\) == len\(data\)"
with pytest.raises(AssertionError, match=msg):
    ts.groupby(lambda key: key[0:6])
