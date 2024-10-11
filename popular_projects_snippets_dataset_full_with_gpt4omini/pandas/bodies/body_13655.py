# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
cidx = MultiIndex.from_tuples([("Z", "a"), ("Z", "b"), ("Y", "c")])
ridx = MultiIndex.from_tuples([("A", "a"), ("A", "b"), ("B", "c")])
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=ridx, columns=cidx)
styler = df.style

default_html = styler.to_html()  # defaults under pd.options to (True , True)

with option_context(
    "styler.sparse.index", sparse_index, "styler.sparse.columns", sparse_columns
):
    html1 = styler.to_html()
    assert (html1 == default_html) is (sparse_index and sparse_columns)
html2 = styler.to_html(sparse_index=sparse_index, sparse_columns=sparse_columns)
assert html1 == html2
