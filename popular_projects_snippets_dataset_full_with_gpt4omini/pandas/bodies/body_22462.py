# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        The transpose of the DataFrame.

        Returns
        -------
        DataFrame
            The transposed DataFrame.

        See Also
        --------
        DataFrame.transpose : Transpose index and columns.

        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df
           col1  col2
        0     1     3
        1     2     4

        >>> df.T
              0  1
        col1  1  2
        col2  3  4
        """
exit(self.transpose())
