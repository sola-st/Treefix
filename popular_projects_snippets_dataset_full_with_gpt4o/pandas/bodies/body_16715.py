# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# https://github.com/pandas-dev/pandas/issues/27943
data1 = DataFrame(
    np.arange(20).reshape((4, 5)) + 1, columns=["a", "b", "c", "d", "e"]
)
data2 = DataFrame(
    np.arange(20).reshape((5, 4)) + 1, columns=["a", "b", "x", "y"]
)

# make each underlying block array / column array read-only
for arr in data1._mgr.arrays:
    arr.flags.writeable = False

data1.merge(data2)  # no error
