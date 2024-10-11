# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_bar.py
# test different align cases for all positive values
result = df_pos.style.bar(align=align)._compute().ctx
expected = {(0, 0): exp[0], (1, 0): exp[1], (2, 0): exp[2]}
assert result == expected
