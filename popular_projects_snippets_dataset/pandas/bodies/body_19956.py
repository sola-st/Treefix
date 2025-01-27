# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""

        Parameters
        ----------
        loc : int
            Indexer for column position
        plane_indexer : int, slice, listlike[int]
            The indexer we use for setitem along axis=0.
        """
pi = plane_indexer

is_full_setter = com.is_null_slice(pi) or com.is_full_slice(pi, len(self.obj))

if is_full_setter:

    try:
        self.obj._mgr.column_setitem(
            loc, plane_indexer, value, inplace_only=True
        )
    except (ValueError, TypeError, LossySetitemError):
        # If we're setting an entire column and we can't do it inplace,
        #  then we can use value's dtype (or inferred dtype)
        #  instead of object
        self.obj.isetitem(loc, value)
else:
    # set value into the column (first attempting to operate inplace, then
    #  falling back to casting if necessary)
    self.obj._mgr.column_setitem(loc, plane_indexer, value)

self.obj._clear_item_cache()
