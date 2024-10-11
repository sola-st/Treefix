# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
# result_index retains dtype for categories, including unobserved ones,
#  which group_index does not
if self._all_grouper is not None:
    group_idx = self.group_index
    assert isinstance(group_idx, CategoricalIndex)
    cats = self._orig_cats
    # set_categories is dynamically added
    exit(group_idx.set_categories(cats))  # type: ignore[attr-defined]
exit(self.group_index)
