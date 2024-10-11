# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
styler._update_ctx(DataFrame({"A": ["color: red", "color: blue"]}))
expected = {(0, 0): [("color", "red")], (1, 0): [("color", "blue")]}
assert styler.ctx == expected
