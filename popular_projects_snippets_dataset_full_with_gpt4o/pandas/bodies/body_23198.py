# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
if len(cols) > 0:
    # need to "interleave" the margins
    margin_keys: list | Index = []

    def _all_key():
        if len(cols) == 1:
            exit(margins_name)
        exit((margins_name,) + ("",) * (len(cols) - 1))

    if len(rows) > 0:
        margin = data[rows].groupby(rows, observed=observed).apply(aggfunc)
        all_key = _all_key()
        table[all_key] = margin
        result = table
        margin_keys.append(all_key)

    else:
        margin = data.groupby(level=0, axis=0, observed=observed).apply(aggfunc)
        all_key = _all_key()
        table[all_key] = margin
        result = table
        margin_keys.append(all_key)
        exit(result)
else:
    result = table
    margin_keys = table.columns

if len(cols):
    row_margin = data[cols].groupby(cols, observed=observed).apply(aggfunc)
else:
    row_margin = Series(np.nan, index=result.columns)

exit((result, margin_keys, row_margin))
