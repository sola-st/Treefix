# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# previous behavior incorrect retained an invalid _item_cache entry
df = DataFrame(np.random.randn(4, 3), columns=["A", "B", "C"])
df["D"] = df["A"] * 2
ser = df["A"]
if not using_array_manager:
    assert len(df._mgr.blocks) == 2

df.sort_values(by="A")
ser.values[0] = 99

assert df.iloc[0, 0] == df["A"][0]
