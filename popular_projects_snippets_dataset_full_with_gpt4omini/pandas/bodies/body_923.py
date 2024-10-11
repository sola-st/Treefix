# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iat.py
# GH#45684
data = {"x": np.arange(8, dtype=np.int64), "y": np.int64(0)}
df = DataFrame(data).copy()
ser = df["y"]

# previously this iat setting would split the block and fail to clear
#  the item_cache.
indexer_ial(df)[7, 0] = 9999

indexer_ial(df)[7, 1] = 1234

assert df.iat[7, 1] == 1234
if not using_copy_on_write:
    assert ser.iloc[-1] == 1234
assert df.iloc[-1, -1] == 1234
