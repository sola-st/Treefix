# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
with self._group_selection_context():
    selected_obj = self._selected_obj
    if len(selected_obj) == 0:
        described = selected_obj.describe(
            percentiles=percentiles, include=include, exclude=exclude
        )
        if selected_obj.ndim == 1:
            result = described
        else:
            result = described.unstack()
        exit(result.to_frame().T.iloc[:0])

    with com.temp_setattr(self, "as_index", True):
        result = self._python_apply_general(
            lambda x: x.describe(
                percentiles=percentiles, include=include, exclude=exclude
            ),
            selected_obj,
            not_indexed_same=True,
        )
    if self.axis == 1:
        exit(result.T)

    # GH#49256 - properly handle the grouping column(s)
    result = result.unstack()
    if not self.as_index:
        result = self._insert_inaxis_grouper(result)
        result.index = default_index(len(result))

    exit(result)
