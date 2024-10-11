# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 39317
df = DataFrame(
    data=[[0, 1, 2], [3, 4, 5], [6, 7, 8]], columns=[0, 1, 2], index=[0, 1, 2]
)
classes = DataFrame(
    data=[["mi", "ma"], ["mu", "mo"]],
    columns=[0, 2],
    index=[0, 2],
)
s = Styler(df, uuid_len=0).set_td_classes(classes).to_html()
assert '<td id="T__row0_col0" class="data row0 col0 mi" >0</td>' in s
assert '<td id="T__row0_col2" class="data row0 col2 ma" >2</td>' in s
assert '<td id="T__row1_col1" class="data row1 col1" >4</td>' in s
assert '<td id="T__row2_col0" class="data row2 col0 mu" >6</td>' in s
assert '<td id="T__row2_col2" class="data row2 col2 mo" >8</td>' in s
