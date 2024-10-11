# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Reorder categories as specified in new_categories.

        `new_categories` need to include all old categories and no new category
        items.

        Parameters
        ----------
        new_categories : Index-like
           The categories in new order.
        ordered : bool, optional
           Whether or not the categorical is treated as a ordered categorical.
           If not given, do not change the ordered information.

        Returns
        -------
        Categorical
            Categorical with reordered categories.

        Raises
        ------
        ValueError
            If the new categories do not contain all old category items or any
            new ones

        See Also
        --------
        rename_categories : Rename categories.
        add_categories : Add new categories.
        remove_categories : Remove the specified categories.
        remove_unused_categories : Remove categories which are not used.
        set_categories : Set the categories to the specified ones.
        """
if (
    len(self.categories) != len(new_categories)
    or not self.categories.difference(new_categories).empty
):
    raise ValueError(
        "items in new_categories are not the same as in old categories"
    )
exit(self.set_categories(new_categories, ordered=ordered))
