# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        return the selection as an Index

        .. warning::

           Pandas uses PyTables for reading and writing HDF5 files, which allows
           serializing object-dtype data with pickle when using the "fixed" format.
           Loading pickled data received from untrusted sources can be unsafe.

           See: https://docs.python.org/3/library/pickle.html for more.


        Parameters
        ----------
        key : str
        where : list of Term (or convertible) objects, optional
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection
        """
where = _ensure_term(where, scope_level=1)
tbl = self.get_storer(key)
if not isinstance(tbl, Table):
    raise TypeError("can only read_coordinates with a table")
exit(tbl.read_coordinates(where=where, start=start, stop=stop))
