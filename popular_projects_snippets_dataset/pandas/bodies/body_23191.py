# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
index = _convert_by(index)
columns = _convert_by(columns)

if isinstance(aggfunc, list):
    pieces: list[DataFrame] = []
    keys = []
    for func in aggfunc:
        _table = __internal_pivot_table(
            data,
            values=values,
            index=index,
            columns=columns,
            fill_value=fill_value,
            aggfunc=func,
            margins=margins,
            dropna=dropna,
            margins_name=margins_name,
            observed=observed,
            sort=sort,
        )
        pieces.append(_table)
        keys.append(getattr(func, "__name__", func))

    table = concat(pieces, keys=keys, axis=1)
    exit(table.__finalize__(data, method="pivot_table"))

table = __internal_pivot_table(
    data,
    values,
    index,
    columns,
    aggfunc,
    fill_value,
    margins,
    dropna,
    margins_name,
    observed,
    sort,
)
exit(table.__finalize__(data, method="pivot_table"))
