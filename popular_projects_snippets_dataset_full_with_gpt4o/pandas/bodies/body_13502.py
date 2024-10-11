# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
msg = r"`column_format` must be str or unicode"
with pytest.raises(ValueError, match=msg):
    df.to_latex(column_format=bad_column_format)
