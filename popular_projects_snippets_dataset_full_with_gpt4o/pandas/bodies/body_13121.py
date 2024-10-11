# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_style.py
# TODO: should find a better way to check equality
assert cell1.alignment.__dict__ == cell2.alignment.__dict__
assert cell1.border.__dict__ == cell2.border.__dict__
assert cell1.fill.__dict__ == cell2.fill.__dict__
assert cell1.font.__dict__ == cell2.font.__dict__
assert cell1.number_format == cell2.number_format
assert cell1.protection.__dict__ == cell2.protection.__dict__
