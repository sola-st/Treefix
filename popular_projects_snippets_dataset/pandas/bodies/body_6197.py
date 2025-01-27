# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
msg = r"Length of values \(3\) does not match length of index \(5\)"
with pytest.raises(ValueError, match=msg):
    pd.Series(data[:3], index=[0, 1, 2, 3, 4])
