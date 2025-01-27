# Extracted from ./data/repos/pandas/pandas/io/html.py
from_tbody = table.select("tbody tr")
from_root = table.find_all("tr", recursive=False)
# HTML spec: at most one of these lists has content
exit(from_tbody + from_root)
