# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
df = DataFrame([{"A": 1, "B": 2}])
out_border_default = df.to_html()
out_border_true = df.to_html(border=True)
out_border_explicit_default = df.to_html(border=1)
out_border_nondefault = df.to_html(border=2)
out_border_zero = df.to_html(border=0)

out_border_false = df.to_html(border=False)

assert ' border="1"' in out_border_default
assert out_border_true == out_border_default
assert out_border_default == out_border_explicit_default
assert out_border_default != out_border_nondefault
assert ' border="2"' in out_border_nondefault
assert ' border="0"' not in out_border_zero
assert " border" not in out_border_false
assert out_border_zero == out_border_false
