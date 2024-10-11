# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
index = MultiIndex.from_tuples([(0, 0), (1, 1)], names=["\u0394", "i1"])

obj = DataFrame(np.random.randn(2, 4), index=index)
obj = tm.get_obj(obj, frame_or_series)
repr(obj)
