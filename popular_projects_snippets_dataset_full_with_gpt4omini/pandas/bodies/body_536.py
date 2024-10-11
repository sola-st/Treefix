# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
c1 = CategoricalDtype(["a", "b"], ordered=ordered)
assert str(c1) == "category"
# Py2 will have unicode prefixes
pat = r"CategoricalDtype\(categories=\[.*\], ordered={ordered}\)"
assert re.match(pat.format(ordered=ordered), repr(c1))
