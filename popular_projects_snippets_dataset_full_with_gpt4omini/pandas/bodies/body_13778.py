# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
attrs = DataFrame({"A": ["color: red; foo: bar", "color:blue ; foo: baz;"]})
styler._update_ctx(attrs)
expected = {
    (0, 0): [("color", "red"), ("foo", "bar")],
    (1, 0): [("color", "blue"), ("foo", "baz")],
}
assert styler.ctx == expected
