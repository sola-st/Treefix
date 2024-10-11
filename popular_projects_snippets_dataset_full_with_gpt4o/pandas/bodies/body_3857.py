# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# big mixed
biggie = DataFrame(
    {"A": np.random.randn(200), "B": tm.makeStringIndex(200)}, index=range(200)
)
biggie.loc[:20, "A"] = np.nan
biggie.loc[:20, "B"] = np.nan

repr(biggie)
