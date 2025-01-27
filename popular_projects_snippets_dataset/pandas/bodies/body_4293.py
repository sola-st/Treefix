# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#27415
op = all_arithmetic_operators
ind = pd.CategoricalIndex(pd.interval_range(start=0.0, end=2.0))
data = [1, 2]
df = DataFrame([data], columns=ind)
num = 10
result = getattr(df, op)(num)
expected = DataFrame([[getattr(n, op)(num) for n in data]], columns=ind)
tm.assert_frame_equal(result, expected)
