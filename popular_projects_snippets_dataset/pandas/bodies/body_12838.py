# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH 35849
# Testing that resulting output reads in as expected.
# Testing one new column, one old column, new rows
df1 = DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
df3 = DataFrame({"col2": ["e", "f"], "col3": ["!", "#"]})

expected = DataFrame(
    {
        "col1": [1, 2, None, None],
        "col2": ["a", "b", "e", "f"],
        "col3": [None, None, "!", "#"],
    }
)
with tm.ensure_clean("test.json") as path:
    # Save dataframes to the same file
    df1.to_json(path, mode="a", lines=True, orient="records")
    df3.to_json(path, mode="a", lines=True, orient="records")

    # Read path file
    result = read_json(path, lines=True)
    tm.assert_frame_equal(result, expected)
