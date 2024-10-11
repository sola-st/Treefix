# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
resolve = CSSResolver()
actual = resolve(css, inherited=inherited)
assert props == actual
