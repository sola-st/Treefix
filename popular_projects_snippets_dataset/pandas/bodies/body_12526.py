# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
rng = date_range("2000-01-01", periods=10)
df = DataFrame(np.random.randn(10, 4), index=rng)

result = df.to_html()
assert "2000-01-01" in result
