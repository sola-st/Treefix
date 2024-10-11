# Extracted from ./data/repos/pandas/pandas/tests/util/test_doc.py
docstr = dedent(
    """
        This is the cumsum method.

        It computes the cumulative sum.
        """
)
assert cumsum.__doc__ == docstr
