# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Check that ser.iloc[i_slc] matches ser.loc[l_slc] and, if applicable,
    ser[l_slc].
    """
expected = ser.iloc[i_slc]

assert_series_equal(ser.loc[l_slc], expected)

if not is_integer_dtype(ser.index):
    # For integer indices, .loc and plain getitem are position-based.
    assert_series_equal(ser[l_slc], expected)
