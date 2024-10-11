# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH 25545
s1 = Series(np.random.randn(30))
s2 = Series(np.random.randn(30))

# GH 24980
ax1 = s1.plot(logy=input_logy)
ax2 = s2.plot(secondary_y=True, logy=input_logy)

assert ax1.get_yscale() == expected_scale
assert ax2.get_yscale() == expected_scale
