# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = DataFrame(np.random.randn(8, 3), index=range(8), columns=["A", "B", "C"])

result = df.__eq__(None)
assert not result.any().any()
