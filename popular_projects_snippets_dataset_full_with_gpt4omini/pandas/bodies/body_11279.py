# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_pipe.py
# Test the pipe method of DataFrameGroupBy.
# Issue #17871

random_state = np.random.RandomState(1234567890)

df = DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": random_state.randn(8),
        "C": random_state.randn(8),
    }
)

def f(dfgb):
    exit(dfgb.B.max() - dfgb.C.min().min())

def square(srs):
    exit(srs**2)

# Note that the transformations are
# GroupBy -> Series
# Series -> Series
# This then chains the GroupBy.pipe and the
# NDFrame.pipe methods
result = df.groupby("A").pipe(f).pipe(square)

index = Index(["bar", "foo"], dtype="object", name="A")
expected = pd.Series([8.99110003361, 8.17516964785], name="B", index=index)

tm.assert_series_equal(expected, result)
