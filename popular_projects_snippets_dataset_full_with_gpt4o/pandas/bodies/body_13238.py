# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_sas7bdat.py
# GH 18198
fname = datapath("io", "sas", "data", "zero_rows.sas7bdat")
result = pd.read_sas(fname)
expected = pd.DataFrame([{"char_field": "a", "num_field": 1.0}]).iloc[:0]
tm.assert_frame_equal(result, expected)
