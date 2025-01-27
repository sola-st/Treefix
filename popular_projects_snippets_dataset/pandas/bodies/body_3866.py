# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
df = DataFrame(np.random.randn(10, 20), columns=tm.rands_array(10, 20))
repr(df)
