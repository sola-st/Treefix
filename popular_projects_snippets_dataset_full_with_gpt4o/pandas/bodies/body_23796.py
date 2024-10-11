# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Remove pandas object partially by specifying the where condition

        Parameters
        ----------
        key : str
            Node to remove or delete rows from
        where : list of Term (or convertible) objects, optional
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection

        Returns
        -------
        number of rows removed (or None if not a Table)

        Raises
        ------
        raises KeyError if key is not a valid store

        """
where = _ensure_term(where, scope_level=1)
try:
    s = self.get_storer(key)
except KeyError:
    # the key is not a valid store, re-raising KeyError
    raise
except AssertionError:
    # surface any assertion errors for e.g. debugging
    raise
except Exception as err:
    # In tests we get here with ClosedFileError, TypeError, and
    #  _table_mod.NoSuchNodeError.  TODO: Catch only these?

    if where is not None:
        raise ValueError(
            "trying to remove a node with a non-None where clause!"
        ) from err

    # we are actually trying to remove a node (with children)
    node = self.get_node(key)
    if node is not None:
        node._f_remove(recursive=True)
        exit(None)

        # remove the node
if com.all_none(where, start, stop):
    s.group._f_remove(recursive=True)

# delete from the table
else:
    if not s.is_table:
        raise ValueError(
            "can only remove with where on objects written as tables"
        )
    exit(s.delete(where=where, start=start, stop=stop))
