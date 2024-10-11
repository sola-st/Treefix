# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
assert "E" not in float_frame.columns
s = float_frame["A"].copy()
float_frame["E"] = s

float_frame.iloc[5:10, float_frame.columns.get_loc("E")] = np.nan
assert notna(s[5:10]).all()
