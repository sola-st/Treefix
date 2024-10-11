# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
exp_index = a.index.union(b.index)
a = a.reindex(exp_index)
b = b.reindex(exp_index)

amask = isna(a)
bmask = isna(b)

exp_values = []
for i in range(len(exp_index)):
    with np.errstate(all="ignore"):
        if amask[i]:
            if bmask[i]:
                exp_values.append(np.nan)
                continue
            exp_values.append(op(fill_value, b[i]))
        elif bmask[i]:
            if amask[i]:
                exp_values.append(np.nan)
                continue
            exp_values.append(op(a[i], fill_value))
        else:
            exp_values.append(op(a[i], b[i]))

result = meth(a, b, fill_value=fill_value)
expected = Series(exp_values, exp_index)
tm.assert_series_equal(result, expected)
