# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
resolve = CSSResolver()
resolved1 = resolve(css1, inherited=inherited)
resolved2 = resolve(css2, inherited=inherited)
assert resolved1 == resolved2
