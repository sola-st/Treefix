# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH 35849
# Testing that resulting output reads in as expected.
# Testing same columns, new rows
df1 = DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
df2 = DataFrame({"col1": [3, 4], "col2": ["c", "d"]})

expected = DataFrame({"col1": [1, 2, 3, 4], "col2": ["a", "b", "c", "d"]})
with tm.ensure_clean("test.json") as path:
    # Save dataframes to the same file
    df1.to_json(path, lines=True, orient="records")
    df2.to_json(path, mode="a", lines=True, orient="records")

    # Read path file
    result = read_json(path, lines=True)
    tm.assert_frame_equal(result, expected)
