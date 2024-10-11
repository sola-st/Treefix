# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_analytics.py
# GH 25303
cat = Categorical(values, categories=categories, ordered=True)
result = getattr(cat, function)(skipna=skipna)

if skipna is False:
    assert result is np.nan
else:
    expected = categories[0] if function == "min" else categories[2]
    assert result == expected
