# Extracted from ./data/repos/pandas/pandas/tests/util/test_doc.py
docstr = dedent(
    """
        This is the cummax method.

        It computes the cumulative maximum.
        """
)
assert cummax.__doc__ == docstr
