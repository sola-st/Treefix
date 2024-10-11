# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
tda_nano = tda.astype("m8[ns]")

expected = tda_nano * 2
res = tda_nano + tda
tm.assert_extension_array_equal(res, expected)
res = tda + tda_nano
tm.assert_extension_array_equal(res, expected)

expected = tda_nano * 0
res = tda - tda_nano
tm.assert_extension_array_equal(res, expected)

res = tda_nano - tda
tm.assert_extension_array_equal(res, expected)
