# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH: 37452
df = DataFrame(
    {"A": [1.0e-20, 2.0e-20, 3.0e-20], "B": [1.0e-20, 2.0e-20, 3.0e-20]}
)
result = df.corr()
expected = DataFrame({"A": [1.0, 1.0], "B": [1.0, 1.0]}, index=["A", "B"])
tm.assert_frame_equal(result, expected)
