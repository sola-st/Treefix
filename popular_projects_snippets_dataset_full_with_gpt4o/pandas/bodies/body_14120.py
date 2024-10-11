# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
"""Check that display logic is correct.

        GH #37359

        See description here:
        https://pandas.pydata.org/docs/dev/user_guide/options.html#frequently-used-options
        """
formatter = fmt.DataFrameFormatter(
    DataFrame(np.random.rand(length, 3)),
    max_rows=max_rows,
    min_rows=min_rows,
)
result = formatter.max_rows_fitted
assert result == expected
