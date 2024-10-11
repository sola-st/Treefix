# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Copy the existing store to a new file, updating in place.

        Parameters
        ----------
        propindexes : bool, default True
            Restore indexes in copied file.
        keys : list, optional
            List of keys to include in the copy (defaults to all).
        overwrite : bool, default True
            Whether to overwrite (remove and replace) existing nodes in the new store.
        mode, complib, complevel, fletcher32 same as in HDFStore.__init__

        Returns
        -------
        open file handle of the new store
        """
new_store = HDFStore(
    file, mode=mode, complib=complib, complevel=complevel, fletcher32=fletcher32
)
if keys is None:
    keys = list(self.keys())
if not isinstance(keys, (tuple, list)):
    keys = [keys]
for k in keys:
    s = self.get_storer(k)
    if s is not None:

        if k in new_store:
            if overwrite:
                new_store.remove(k)

        data = self.select(k)
        if isinstance(s, Table):

            index: bool | list[str] = False
            if propindexes:
                index = [a.name for a in s.axes if a.is_indexed]
            new_store.append(
                k,
                data,
                index=index,
                data_columns=getattr(s, "data_columns", None),
                encoding=s.encoding,
            )
        else:
            new_store.put(k, data, encoding=s.encoding)

exit(new_store)
