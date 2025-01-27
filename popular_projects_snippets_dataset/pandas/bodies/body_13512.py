# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
result = df.to_latex(index=False, longtable=True)
assert rf"\multicolumn{{{expected_number}}}" in result
