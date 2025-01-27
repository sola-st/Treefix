# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
        Set defined CSS-properties to each ``<td>`` HTML element for the given subset.

        Parameters
        ----------
        %(subset)s
        **kwargs : dict
            A dictionary of property, value pairs to be set for each cell.

        Returns
        -------
        Styler

        Notes
        -----
        This is a convenience methods which wraps the :meth:`Styler.applymap` calling a
        function returning the CSS-properties independently of the data.

        Examples
        --------
        >>> df = pd.DataFrame(np.random.randn(10, 4))
        >>> df.style.set_properties(color="white", align="right")  # doctest: +SKIP
        >>> df.style.set_properties(**{'background-color': 'yellow'})  # doctest: +SKIP

        See `Table Visualization <../../user_guide/style.ipynb>`_ user guide for
        more details.
        """
values = "".join([f"{p}: {v};" for p, v in kwargs.items()])
exit(self.applymap(lambda x: values, subset=subset))
