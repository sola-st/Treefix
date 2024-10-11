# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
index = ["foo", "bar", "baz"]
df = DataFrame(
    {"A": [1, 2, 3], "B": [1.2, 3.4, 5.6], "C": ["one", "two", np.nan]},
    columns=["A", "B", "C"],
    index=index,
)
exit(df)
