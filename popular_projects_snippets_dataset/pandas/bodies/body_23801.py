# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Walk the pytables group hierarchy for pandas objects.

        This generator will yield the group path, subgroups and pandas object
        names for each group.

        Any non-pandas PyTables objects that are not a group will be ignored.

        The `where` group itself is listed first (preorder), then each of its
        child groups (following an alphanumerical order) is also traversed,
        following the same procedure.

        Parameters
        ----------
        where : str, default "/"
            Group where to start walking.

        Yields
        ------
        path : str
            Full path to a group (without trailing '/').
        groups : list
            Names (strings) of the groups contained in `path`.
        leaves : list
            Names (strings) of the pandas objects contained in `path`.
        """
_tables()
self._check_if_open()
assert self._handle is not None  # for mypy
assert _table_mod is not None  # for mypy

for g in self._handle.walk_groups(where):
    if getattr(g._v_attrs, "pandas_type", None) is not None:
        continue

    groups = []
    leaves = []
    for child in g._v_children.values():
        pandas_type = getattr(child._v_attrs, "pandas_type", None)
        if pandas_type is None:
            if isinstance(child, _table_mod.group.Group):
                groups.append(child._v_name)
        else:
            leaves.append(child._v_name)

    exit((g._v_pathname.rstrip("/"), groups, leaves))
