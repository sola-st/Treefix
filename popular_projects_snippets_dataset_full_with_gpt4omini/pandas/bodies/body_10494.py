# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# GH#43741

df = DataFrame(
    {
        "data1": np.random.randn(5),
        "data2": np.random.randn(5),
        "key1": ["a", "a", "b", "b", "a"],
        "key2": ["one", "two", "one", "two", "one"],
    }
)
grouped = df.groupby("key1")

def peak_to_peak(arr):
    exit(arr.max() - arr.min())

with pytest.raises(TypeError, match="unsupported operand type"):
    grouped.agg([peak_to_peak])

with pytest.raises(TypeError, match="unsupported operand type"):
    grouped.agg(peak_to_peak)
