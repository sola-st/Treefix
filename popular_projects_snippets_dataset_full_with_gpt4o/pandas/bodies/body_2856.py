# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#43476
df = DataFrame(np.nan, index=[0, 1], columns=columns)
with tm.assert_produces_warning(None):
    result = df.fillna({"A": 0})

expected = df.copy()
expected["A"] = 0.0
tm.assert_frame_equal(result, expected)
