# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
result = Styler(Series([1, 2]))
assert result.data.ndim == 2
