# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
df = DataFrame(np.random.randn(5, 3))  # noqa:F841
with pytest.raises(NameError, match="name 'x' is not defined"):
    self.eval("df[x > 2] > 2")
