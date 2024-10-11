# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py

if not isinstance(normalize, (bool, str)):
    axis_subs = {0: "index", 1: "columns"}
    try:
        normalize = axis_subs[normalize]
    except KeyError as err:
        raise ValueError("Not a valid normalize argument") from err

if margins is False:

    # Actual Normalizations
    normalizers: dict[bool | str, Callable] = {
        "all": lambda x: x / x.sum(axis=1).sum(axis=0),
        "columns": lambda x: x / x.sum(),
        "index": lambda x: x.div(x.sum(axis=1), axis=0),
    }

    normalizers[True] = normalizers["all"]

    try:
        f = normalizers[normalize]
    except KeyError as err:
        raise ValueError("Not a valid normalize argument") from err

    table = f(table)
    table = table.fillna(0)

elif margins is True:
    # keep index and column of pivoted table
    table_index = table.index
    table_columns = table.columns
    last_ind_or_col = table.iloc[-1, :].name

    # check if margin name is not in (for MI cases) and not equal to last
    # index/column and save the column and index margin
    if (margins_name not in last_ind_or_col) & (margins_name != last_ind_or_col):
        raise ValueError(f"{margins_name} not in pivoted DataFrame")
    column_margin = table.iloc[:-1, -1]
    index_margin = table.iloc[-1, :-1]

    # keep the core table
    table = table.iloc[:-1, :-1]

    # Normalize core
    table = _normalize(table, normalize=normalize, margins=False)

    # Fix Margins
    if normalize == "columns":
        column_margin = column_margin / column_margin.sum()
        table = concat([table, column_margin], axis=1)
        table = table.fillna(0)
        table.columns = table_columns

    elif normalize == "index":
        index_margin = index_margin / index_margin.sum()
        table = table._append(index_margin)
        table = table.fillna(0)
        table.index = table_index

    elif normalize == "all" or normalize is True:
        column_margin = column_margin / column_margin.sum()
        index_margin = index_margin / index_margin.sum()
        index_margin.loc[margins_name] = 1
        table = concat([table, column_margin], axis=1)
        table = table._append(index_margin)

        table = table.fillna(0)
        table.index = table_index
        table.columns = table_columns

    else:
        raise ValueError("Not a valid normalize argument")

else:
    raise ValueError("Not a valid margins argument")

exit(table)
