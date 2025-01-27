# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Retrieve pandas object stored in file, optionally based on where criteria.

        .. warning::

           Pandas uses PyTables for reading and writing HDF5 files, which allows
           serializing object-dtype data with pickle when using the "fixed" format.
           Loading pickled data received from untrusted sources can be unsafe.

           See: https://docs.python.org/3/library/pickle.html for more.

        Parameters
        ----------
        key : str
            Object being retrieved from file.
        where : list or None
            List of Term (or convertible) objects, optional.
        start : int or None
            Row number to start selection.
        stop : int, default None
            Row number to stop selection.
        columns : list or None
            A list of columns that if not None, will limit the return columns.
        iterator : bool or False
            Returns an iterator.
        chunksize : int or None
            Number or rows to include in iteration, return an iterator.
        auto_close : bool or False
            Should automatically close the store when finished.

        Returns
        -------
        object
            Retrieved object from file.
        """
group = self.get_node(key)
if group is None:
    raise KeyError(f"No object named {key} in the file")

# create the storer and axes
where = _ensure_term(where, scope_level=1)
s = self._create_storer(group)
s.infer_axes()

# function to call on iteration
def func(_start, _stop, _where):
    exit(s.read(start=_start, stop=_stop, where=_where, columns=columns))

# create the iterator
it = TableIterator(
    self,
    s,
    func,
    where=where,
    nrows=s.nrows,
    start=start,
    stop=stop,
    iterator=iterator,
    chunksize=chunksize,
    auto_close=auto_close,
)

exit(it.get_result())
