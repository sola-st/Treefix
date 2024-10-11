# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 35607
df = DataFrame(data=[[0, 1], [1, 2]], columns=["A", "B"])
styler = df.style.set_table_styles(
    [{"selector": "", "props": [("background-color", "yellow")]}]
).set_table_styles(
    [{"selector": ".col0", "props": [("background-color", "blue")]}],
    overwrite=False,
)
assert len(styler.table_styles) == 2
