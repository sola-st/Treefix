# Extracted from ./data/repos/pandas/pandas/tests/util/test_doc.py
docstr = dedent(
    """
        This is the cumavg method.

        It computes the cumulative average.

        Examples
        --------

        >>> cumavg([1, 2, 3])
        2
        """
)
assert cumavg.__doc__ == docstr
