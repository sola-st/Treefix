# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 36345
df = DataFrame(data=[["A"]])
s = Styler(df, uuid_len=len_, cell_ids=False).to_html()
strt = s.find('id="T_')
end = s[strt + 6 :].find('"')
if len_ > 32:
    assert end == 32
else:
    assert end == len_
