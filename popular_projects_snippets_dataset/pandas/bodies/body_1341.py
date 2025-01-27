# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

# multi axis slicing issue with single block
# surfaced in GH 6059

arr = np.random.randn(6, 4)
index = date_range("20130101", periods=6)
columns = list("ABCD")
df = DataFrame(arr, index=index, columns=columns)

# defines ref_locs
df.describe()

result = df.iloc[3:5, 0:2]
str(result)
result.dtypes

expected = DataFrame(arr[3:5, 0:2], index=index[3:5], columns=columns[0:2])
tm.assert_frame_equal(result, expected)

# for dups
df.columns = list("aaaa")
result = df.iloc[3:5, 0:2]
str(result)
result.dtypes

expected = DataFrame(arr[3:5, 0:2], index=index[3:5], columns=list("aa"))
tm.assert_frame_equal(result, expected)

# related
arr = np.random.randn(6, 4)
index = list(range(0, 12, 2))
columns = list(range(0, 8, 2))
df = DataFrame(arr, index=index, columns=columns)

if not using_array_manager:
    df._mgr.blocks[0].mgr_locs
result = df.iloc[1:5, 2:4]
str(result)
result.dtypes
expected = DataFrame(arr[1:5, 2:4], index=index[1:5], columns=columns[2:4])
tm.assert_frame_equal(result, expected)
