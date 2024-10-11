# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
# GH41108

mock_clipboard[request.node.name] = multiindex[0]
df = read_clipboard()
df_expected = DataFrame(
    data={"col1": [1, None, 2], "col2": ["red", "blue", "green"]},
    index=multiindex[1],
)

# excel data is parsed correctly
tm.assert_frame_equal(df, df_expected)
