# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
assert cls.called_save
assert cls.called_write_cells
assert not cls.called_sheets
cls.called_save = False
cls.called_write_cells = False
