# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH 6114
msg = re.escape(
    "Passing a bool to header is invalid. Use header=None for no header or "
    "header=int or list-like of ints to specify the row(s) making up the "
    "column names"
)
with pytest.raises(TypeError, match=msg):
    self.read_html(spam_data, header=arg)
