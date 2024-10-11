# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
cell = {"attributes": 'colspan="3"', "display_value": "text", "cellstyle": []}
expected = "\\multicolumn{3}{Y}{text}"
assert _parse_latex_header_span(cell, "X", "Y") == expected

cell = {"attributes": 'rowspan="5"', "display_value": "text", "cellstyle": []}
expected = "\\multirow[X]{5}{*}{text}"
assert _parse_latex_header_span(cell, "X", "Y") == expected

cell = {"display_value": "text", "cellstyle": []}
assert _parse_latex_header_span(cell, "X", "Y") == "text"

cell = {"display_value": "text", "cellstyle": [("bfseries", "--rwrap")]}
assert _parse_latex_header_span(cell, "X", "Y") == "\\bfseries{text}"
