# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
with tm.ensure_clean() as path:
    df = DataFrame(np.random.randn(10, 2), columns=list("AB"))
    df.to_stata(path)
