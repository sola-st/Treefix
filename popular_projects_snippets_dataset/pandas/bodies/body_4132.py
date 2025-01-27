# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
for k, v in float_frame.iterrows():
    exp = float_frame.loc[k]
    tm.assert_series_equal(v, exp)

for k, v in float_string_frame.iterrows():
    exp = float_string_frame.loc[k]
    tm.assert_series_equal(v, exp)
