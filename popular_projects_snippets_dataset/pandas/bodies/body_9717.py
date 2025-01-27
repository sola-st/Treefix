# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

# on/index must be monotonic
df = DataFrame(
    {"A": date_range("20130101", periods=5, freq="s"), "B": range(5)}
)

assert df.A.is_monotonic_increasing
df.rolling("2s", on="A").sum()

df = df.set_index("A")
assert df.index.is_monotonic_increasing
df.rolling("2s").sum()
