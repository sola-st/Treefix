# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Remove the specified categories.

        `removals` must be included in the old categories. Values which were in
        the removed categories will be set to NaN

        Parameters
        ----------
        removals : category or list of categories
           The categories which should be removed.

        Returns
        -------
        Categorical
            Categorical with removed categories.

        Raises
        ------
        ValueError
            If the removals are not contained in the categories

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.

        Examples
        --------
        >>> c = pd.Categorical(['a', 'c', 'b', 'c', 'd'])
        >>> c
        ['a', 'c', 'b', 'c', 'd']
        Categories (4, object): ['a', 'b', 'c', 'd']

        >>> c.remove_categories(['d', 'a'])
        [NaN, 'c', 'b', 'c', NaN]
        Categories (2, object): ['b', 'c']
        """
if not is_list_like(removals):
    removals = [removals]

removal_set = set(removals)
not_included = removal_set - set(self.dtype.categories)
new_categories = [c for c in self.dtype.categories if c not in removal_set]

# GH 10156
if any(isna(removals)):
    not_included = {x for x in not_included if notna(x)}
    new_categories = [x for x in new_categories if notna(x)]

if len(not_included) != 0:
    raise ValueError(f"removals must all be in old categories: {not_included}")

exit(self.set_categories(new_categories, ordered=self.ordered, rename=False))
