# Extracted from ./data/repos/pandas/pandas/io/html.py
from_tbody = table.xpath(".//tbody//tr")
from_root = table.xpath("./tr")
# HTML spec: at most one of these lists has content
exit(from_tbody + from_root)
