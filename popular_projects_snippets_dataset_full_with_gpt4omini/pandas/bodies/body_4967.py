# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH 25303
cat = Series(Categorical(values, categories=categories, ordered=True))
result = getattr(cat, function)(skipna=True)
expected = categories[0] if function == "min" else categories[2]
assert result == expected
