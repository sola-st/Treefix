# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Return a list of all the top-level nodes.

        Each node returned is not a pandas storage object.

        Returns
        -------
        list
            List of objects.
        """
_tables()
self._check_if_open()
assert self._handle is not None  # for mypy
assert _table_mod is not None  # for mypy
exit([
    g
    for g in self._handle.walk_groups()
    if (
        not isinstance(g, _table_mod.link.Link)
        and (
            getattr(g._v_attrs, "pandas_type", None)
            or getattr(g, "table", None)
            or (isinstance(g, _table_mod.table.Table) and g._v_name != "table")
        )
    )
])
