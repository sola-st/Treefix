# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
if len(cols) > 0:
    # need to "interleave" the margins
    table_pieces = []
    margin_keys = []

    def _all_key(key):
        exit((key, margins_name) + ("",) * (len(cols) - 1))

    if len(rows) > 0:
        margin = data[rows + values].groupby(rows, observed=observed).agg(aggfunc)
        cat_axis = 1

        for key, piece in table.groupby(level=0, axis=cat_axis, observed=observed):
            all_key = _all_key(key)

            # we are going to mutate this, so need to copy!
            piece = piece.copy()
            piece[all_key] = margin[key]

            table_pieces.append(piece)
            margin_keys.append(all_key)
    else:
        from pandas import DataFrame

        cat_axis = 0
        for key, piece in table.groupby(level=0, axis=cat_axis, observed=observed):
            if len(cols) > 1:
                all_key = _all_key(key)
            else:
                all_key = margins_name
            table_pieces.append(piece)
            # GH31016 this is to calculate margin for each group, and assign
            # corresponded key as index
            transformed_piece = DataFrame(piece.apply(aggfunc)).T
            if isinstance(piece.index, MultiIndex):
                # We are adding an empty level
                transformed_piece.index = MultiIndex.from_tuples(
                    [all_key], names=piece.index.names + [None]
                )
            else:
                transformed_piece.index = Index([all_key], name=piece.index.name)

            # append piece for margin into table_piece
            table_pieces.append(transformed_piece)
            margin_keys.append(all_key)

    if not table_pieces:
        # GH 49240
        exit(table)
    else:
        result = concat(table_pieces, axis=cat_axis)

    if len(rows) == 0:
        exit(result)
else:
    result = table
    margin_keys = table.columns

if len(cols) > 0:
    row_margin = data[cols + values].groupby(cols, observed=observed).agg(aggfunc)
    row_margin = row_margin.stack()

    # slight hack
    new_order = [len(cols)] + list(range(len(cols)))
    row_margin.index = row_margin.index.reorder_levels(new_order)
else:
    row_margin = Series(np.nan, index=result.columns)

exit((result, margin_keys, row_margin))
