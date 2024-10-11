# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#5818
df = DataFrame(
    [[1, 2], [3, 4]],
    columns=date_range("1/1/2013", "1/2/2013"),
    index=["A", "B"],
)
df.index.name = name

result = df.reset_index()

item = name if name is not None else "index"
columns = Index([item, datetime(2013, 1, 1), datetime(2013, 1, 2)])
if isinstance(item, str) and item == "2012-12-31":
    columns = columns.astype("datetime64[ns]")
else:
    assert columns.dtype == object

expected = DataFrame(
    [["A", 1, 2], ["B", 3, 4]],
    columns=columns,
)
tm.assert_frame_equal(result, expected)
