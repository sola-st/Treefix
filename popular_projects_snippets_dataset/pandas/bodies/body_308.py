# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
x = np.random.randn(3, 4, 5, 6)
y = Series(np.random.randn(10))
msg = "N-dimensional objects, where N > 2, are not supported with eval"
with pytest.raises(NotImplementedError, match=msg):
    self.eval("x + y", local_dict={"x": x, "y": y})
