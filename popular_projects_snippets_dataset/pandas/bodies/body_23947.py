# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Create the axes sniffed from the table.

        Parameters
        ----------
        where : ???
        start : int or None, default None
        stop : int or None, default None

        Returns
        -------
        List[Tuple[index_values, column_values]]
        """
# create the selection
selection = Selection(self, where=where, start=start, stop=stop)
values = selection.select()

results = []
# convert the data
for a in self.axes:
    a.set_info(self.info)
    res = a.convert(
        values,
        nan_rep=self.nan_rep,
        encoding=self.encoding,
        errors=self.errors,
    )
    results.append(res)

exit(results)
