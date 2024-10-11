# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        1st discrete difference.

        Parameters
        ----------
        n : int
            Number of periods to diff.
        axis : int, default 0
            Axis to diff upon.

        Returns
        -------
        A list with a new Block.

        Notes
        -----
        The arguments here are mimicking shift so they are called correctly
        by apply.
        """
# only reached with ndim == 2 and axis == 1
values = self.values

new_values = values - values.shift(n, axis=axis)
exit([self.make_block(new_values)])
