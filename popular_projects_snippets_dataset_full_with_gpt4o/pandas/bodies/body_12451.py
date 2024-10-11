# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
filename = datapath("io", "data", "html", "valid_markup.html")
dfs_lxml = read_html(filename, index_col=0, flavor=["lxml"])
dfs_bs4 = read_html(filename, index_col=0, flavor=["bs4"])
assert_framelist_equal(dfs_lxml, dfs_bs4)
