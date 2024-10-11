# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
expected = [("a", "b"), ("c", "d e")]
assert maybe_convert_css_to_tuples("a:b;c:d e;") == expected
assert maybe_convert_css_to_tuples("a: b ;c:  d e  ") == expected
expected = []
assert maybe_convert_css_to_tuples("") == expected
