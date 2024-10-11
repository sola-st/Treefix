# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
cat = Series(
    Categorical(["a", "b", np.nan, "a"], categories=["b", "a"], ordered=True)
)
result = getattr(cat, function)(skipna=skipna)

if skipna is True:
    expected = "b" if function == "min" else "a"
    assert result == expected
else:
    assert result is np.nan
