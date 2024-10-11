# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH 37705
file_path_string = datapath("io", "data", "html", "spam.html")
file_path = Path(file_path_string)
df1 = self.read_html(file_path_string)[0]
df2 = self.read_html(file_path)[0]
tm.assert_frame_equal(df1, df2)
