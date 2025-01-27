# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
all_data = all_data[:10]
if dropna:
    other = np.array(all_data[~all_data.isna()])
else:
    other = all_data

vcs = pd.Series(all_data).value_counts(dropna=dropna)
vcs_ex = pd.Series(other).value_counts(dropna=dropna)

with decimal.localcontext() as ctx:
    # avoid raising when comparing Decimal("NAN") < Decimal(2)
    ctx.traps[decimal.InvalidOperation] = False

    result = vcs.sort_index()
    expected = vcs_ex.sort_index()

tm.assert_series_equal(result, expected)
