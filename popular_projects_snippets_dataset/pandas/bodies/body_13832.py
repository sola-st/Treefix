# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 36159
df = DataFrame(data=[[0, 1], [2, 3]], columns=["A", "B"], index=["a", "b"])
s = Styler(df, uuid_len=0, cell_ids=False).set_td_classes(classes).to_html()
assert '<td class="data row0 col0" >0</td>' in s
assert '<td class="data row0 col1 test-class" >1</td>' in s
assert '<td class="data row1 col0" >2</td>' in s
assert '<td class="data row1 col1" >3</td>' in s
# GH 39317
s = Styler(df, uuid_len=0, cell_ids=True).set_td_classes(classes).to_html()
assert '<td id="T__row0_col0" class="data row0 col0" >0</td>' in s
assert '<td id="T__row0_col1" class="data row0 col1 test-class" >1</td>' in s
assert '<td id="T__row1_col0" class="data row1 col0" >2</td>' in s
assert '<td id="T__row1_col1" class="data row1 col1" >3</td>' in s
