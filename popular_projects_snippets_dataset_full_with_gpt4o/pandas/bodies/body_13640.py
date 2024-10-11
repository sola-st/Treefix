# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
# GH 36223
df = DataFrame(data=[[1, 2]], columns=[["l0", "l0"], ["l1a", "l1b"]])
styler = Styler(df, uuid="_", cell_ids=False)
assert '<th class="col_heading level0 col0" colspan="2">l0</th>' in styler.to_html()
