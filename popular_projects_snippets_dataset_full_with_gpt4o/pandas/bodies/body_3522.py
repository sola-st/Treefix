# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = DataFrame(
    {
        "A": [datetime(2000, 1, 1) + timedelta(i) for i in range(1000)],
        "B": np.random.randn(1000),
    }
)

idf = df.set_index("A")
assert isinstance(idf.index, DatetimeIndex)
