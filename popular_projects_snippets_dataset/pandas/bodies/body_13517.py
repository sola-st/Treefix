# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
# GH 7124
df = DataFrame({"a": [1, 2], "b": ["b1", "b2"]})
msg = f"Writing 2 cols but got {num_aliases} aliases"
with pytest.raises(ValueError, match=msg):
    df.to_latex(header=header)
