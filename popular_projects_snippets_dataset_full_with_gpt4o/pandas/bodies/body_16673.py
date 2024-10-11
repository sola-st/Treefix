# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
dt = datetime.now()
df1 = DataFrame({"x": ["a"]}, index=[dt])

df2 = DataFrame({"y": ["b", "c"]}, index=[dt, dt])

msg = (
    "No common columns to perform merge on. "
    f"Merge options: left_on={None}, right_on={None}, "
    f"left_index={False}, right_index={False}"
)

with pytest.raises(MergeError, match=msg):
    merge(df1, df2)
