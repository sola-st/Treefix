# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH #27464 make sure we mask 0/1 with Inf and not NaN
df = pd.DataFrame({"A": [0, 1, 2], "B": [1.1, None, 1.1]})

other = pd.DataFrame({"A": [1.1, 1.2, 1.3]}, index=[0, 2, 3])

result = df.rfloordiv(other, fill_value=1)

expected = pd.DataFrame(
    {"A": [np.inf, 1.0, 0.0, 1.0], "B": [0.0, np.nan, 0.0, np.nan]}
)
tm.assert_frame_equal(result, expected)
