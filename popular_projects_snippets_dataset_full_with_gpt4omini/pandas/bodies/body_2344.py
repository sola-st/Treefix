# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_take.py

# mixed-dtype
order = [4, 1, 2, 0, 3]
for df in [float_string_frame]:

    result = df.take(order, axis=0)
    expected = df.reindex(df.index.take(order))
    tm.assert_frame_equal(result, expected)

    # axis = 1
    result = df.take(order, axis=1)
    expected = df.loc[:, ["foo", "B", "C", "A", "D"]]
    tm.assert_frame_equal(result, expected)

# negative indices
order = [4, 1, -2]
for df in [float_string_frame]:

    result = df.take(order, axis=0)
    expected = df.reindex(df.index.take(order))
    tm.assert_frame_equal(result, expected)

    # axis = 1
    result = df.take(order, axis=1)
    expected = df.loc[:, ["foo", "B", "D"]]
    tm.assert_frame_equal(result, expected)
