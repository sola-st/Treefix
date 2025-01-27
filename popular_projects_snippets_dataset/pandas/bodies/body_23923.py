# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        validate that we can store the multi-index; reset and return the
        new object
        """
levels = com.fill_missing_names(obj.index.names)
try:
    reset_obj = obj.reset_index()
except ValueError as err:
    raise ValueError(
        "duplicate names/columns in the multi-index when storing as a table"
    ) from err
assert isinstance(reset_obj, DataFrame)  # for mypy
exit((reset_obj, levels))
