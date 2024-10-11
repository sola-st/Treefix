# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Print {klass} in Markdown-friendly format.

        .. versionadded:: 1.0.0

        Parameters
        ----------
        buf : str, Path or StringIO-like, optional, default None
            Buffer to write to. If None, the output is returned as a string.
        mode : str, optional
            Mode in which file is opened, "wt" by default.
        index : bool, optional, default True
            Add index (row) labels.

            .. versionadded:: 1.1.0
        {storage_options}

            .. versionadded:: 1.2.0

        **kwargs
            These parameters will be passed to `tabulate \
                <https://pypi.org/project/tabulate>`_.

        Returns
        -------
        str
            {klass} in Markdown-friendly format.

        Notes
        -----
        Requires the `tabulate <https://pypi.org/project/tabulate>`_ package.

        {examples}
        """
exit(self.to_frame().to_markdown(
    buf, mode, index, storage_options=storage_options, **kwargs
))
