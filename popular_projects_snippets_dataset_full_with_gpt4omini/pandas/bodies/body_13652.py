# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
if index:
    styler_mi.set_sticky(axis=0)
if columns:
    styler_mi.set_sticky(axis=1)

left_css = (
    "#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n"
    "  left: {1}px;\n  min-width: 75px;\n  max-width: 75px;\n  z-index: {2};\n}}"
)
top_css = (
    "#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n"
    "  top: {1}px;\n  height: 25px;\n  z-index: {2};\n}}"
)

res = styler_mi.set_uuid("").to_html()

# test the index stickys for thead and tbody over both levels
assert (
    left_css.format("thead tr th:nth-child(1)", "0", "3 !important") in res
) is index
assert (left_css.format("tbody tr th.level0", "0", "1") in res) is index
assert (
    left_css.format("thead tr th:nth-child(2)", "75", "3 !important") in res
) is index
assert (left_css.format("tbody tr th.level1", "75", "1") in res) is index

# test the column stickys for each level row
assert (top_css.format("thead tr:nth-child(1) th", "0", "2") in res) is columns
assert (top_css.format("thead tr:nth-child(2) th", "25", "2") in res) is columns
