# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_format.py
# tests the na_rep is not escaped
df = DataFrame([['<>&"', None]])
s = Styler(df, uuid_len=0).format("X&{0}>X", escape="html", na_rep="&")
ex = '<td id="T__row0_col0" class="data row0 col0" >X&&lt;&gt;&amp;&#34;>X</td>'
expected2 = '<td id="T__row0_col1" class="data row0 col1" >&</td>'
assert ex in s.to_html()
assert expected2 in s.to_html()

# also test for format_index()
df = DataFrame(columns=['<>&"', None])
styler = Styler(df, uuid_len=0)
styler.format_index("X&{0}>X", escape="html", na_rep="&", axis=1)
ctx = styler._translate(True, True)
assert ctx["head"][0][1]["display_value"] == "X&&lt;&gt;&amp;&#34;>X"
assert ctx["head"][0][2]["display_value"] == "&"
