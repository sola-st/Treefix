# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
"""
        Method for writing a formatted <th> cell.

        If col_space is set on the formatter then that is used for
        the value of min-width.

        Parameters
        ----------
        s : object
            The data to be written inside the cell.
        header : bool, default False
            Set to True if the <th> is for use inside <thead>.  This will
            cause min-width to be set if there is one.
        indent : int, default 0
            The indentation level of the cell.
        tags : str, default None
            Tags to include in the cell.

        Returns
        -------
        A written <th> cell.
        """
col_space = self.col_space.get(s, None)

if header and col_space is not None:
    tags = tags or ""
    tags += f'style="min-width: {col_space};"'

self._write_cell(s, kind="th", indent=indent, tags=tags)
