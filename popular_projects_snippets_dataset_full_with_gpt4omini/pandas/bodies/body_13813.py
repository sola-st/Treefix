# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
f = lambda x: "color: red" if x > 0 else "color: blue"
g = lambda x, z: f"color: {z}" if x > 0 else f"color: {z}"
style1 = styler
style1.applymap(f).applymap(g, z="b").highlight_max()._compute()  # = render
result = style1.export()
style2 = df.style
style2.use(result)
assert style1._todo == style2._todo
style2.to_html()
