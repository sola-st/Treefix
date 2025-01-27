# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
result = df.style.to_html()  # trim=True
assert result.count("#") == 0

result = df.style.highlight_max().to_html()
assert result.count("#") == len(df.columns)
