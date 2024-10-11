# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# GH#45640
df = DataFrame([[0.2, 0.4], [0.4, 0.2]])
result = df.corr()
expected = DataFrame({0: [1.0, -1.0], 1: [-1.0, 1.0]})
tm.assert_frame_equal(result - 1, expected - 1, atol=1e-17)
