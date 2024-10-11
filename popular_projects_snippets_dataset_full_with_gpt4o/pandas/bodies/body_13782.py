# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
df = DataFrame({"A": [0, 1]})
style = lambda x: Series(
    ["color: red; border: 1px", "color: blue; border: 2px"], name=x.name
)
s = Styler(df, uuid="AB").apply(style)
s.to_html()
