# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH 3624, after appending columns, to_csv fails
with tm.ensure_clean("__tmp_to_csv_no_index__") as path:
    df = DataFrame({"c1": [1, 2, 3], "c2": [4, 5, 6]})
    df.to_csv(path, index=False)
    result = read_csv(path)
    tm.assert_frame_equal(df, result)
    df["c3"] = Series([7, 8, 9], dtype="int64")
    df.to_csv(path, index=False)
    result = read_csv(path)
    tm.assert_frame_equal(df, result)
