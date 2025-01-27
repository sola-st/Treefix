# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
index = PeriodIndex(["2011-1", "2011-2", "2011-3"], freq="M")
frame = DataFrame(np.random.randn(3, 4), index=index)

# it works!
frame.to_string()
