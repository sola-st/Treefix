# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
# GH 47203
result = df.style.to_latex(clines=clines)
assert result == expected
