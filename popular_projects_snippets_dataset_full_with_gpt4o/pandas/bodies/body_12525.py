# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
banklist_data = datapath("io", "data", "html", "banklist.html")

self.read_html(banklist_data, match=".*Water.*", flavor=["lxml", "html5lib"])
