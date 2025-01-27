# Extracted from ./data/repos/pandas/pandas/io/html.py
# Look for direct children only: the "row" element here may be a
# <thead> or <tfoot> (see _parse_thead_tr).
exit(row.xpath("./td|./th"))
