# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 35588
# GH 35663
df = DataFrame(data=[[0]])
styler = Styler(df, uuid="_", cell_ids=False)
styler.to_html()
s = styler.to_html()  # render twice to ensure ctx is not updated
assert s.find('<td class="data row0 col0" >') != -1
