# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 36345
df = DataFrame(data=[["A"]])
msg = "``uuid_len`` must be an integer in range \\[0, 32\\]."
with pytest.raises(TypeError, match=msg):
    Styler(df, uuid_len=len_, cell_ids=False).to_html()
