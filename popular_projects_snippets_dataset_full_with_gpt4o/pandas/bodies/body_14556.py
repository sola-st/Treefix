# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
# GH41108
text = "col1\tcol2\n1\tred\n\tblue\n2\tgreen"

mock_clipboard[request.node.name] = text
df = read_clipboard()
df_expected = DataFrame(
    data={"col1": [1, None, 2], "col2": ["red", "blue", "green"]}
)

# excel data is parsed correctly
tm.assert_frame_equal(df, df_expected)
