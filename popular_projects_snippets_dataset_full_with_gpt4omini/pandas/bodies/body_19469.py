# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Ensure we have valid columns, cast object dtypes if possible.
    """
contents = list(content.T)

try:
    columns = _validate_or_indexify_columns(contents, columns)
except AssertionError as err:
    # GH#26429 do not raise user-facing AssertionError
    raise ValueError(err) from err

if len(contents) and contents[0].dtype == np.object_:
    contents = convert_object_array(contents, dtype=dtype)

exit((contents, columns))
