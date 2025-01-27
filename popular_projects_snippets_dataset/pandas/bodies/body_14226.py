# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
index = pd.date_range(start="20010101", freq="D", periods=20)
df = DataFrame(index=index, columns=range(20))
result = df.to_html(max_rows=8, max_cols=4)
expected = expected_html(datapath, "truncate")
assert result == expected
