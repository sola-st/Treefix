# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# https://github.com/pandas-dev/pandas/issues/19682
# https://github.com/pandas-dev/pandas/issues/13628
cat = Categorical([1, 2, 3, None, None])

if len(fillna_kwargs) == 1 and "value" in fillna_kwargs:
    err = TypeError
else:
    err = ValueError

with pytest.raises(err, match=msg):
    cat.fillna(**fillna_kwargs)
