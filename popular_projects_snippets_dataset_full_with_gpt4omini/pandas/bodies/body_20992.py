# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        The categories of this categorical.

        Setting assigns new values to each category (effectively a rename of
        each individual category).

        The assigned value has to be a list-like object. All items must be
        unique and the number of items in the new categories must be the same
        as the number of items in the old categories.

        Raises
        ------
        ValueError
            If the new categories do not validate as categories or if the
            number of new categories is unequal the number of old categories

        See Also
        --------
        rename_categories : Rename categories.
        reorder_categories : Reorder categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.
        """
exit(self.dtype.categories)
