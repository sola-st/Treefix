# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
test_sers = gen_series_formatting()
for s in test_sers.values():
    self.chck_ncols(s)
