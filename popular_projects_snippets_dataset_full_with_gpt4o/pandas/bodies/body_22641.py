# Extracted from ./data/repos/pandas/pandas/core/frame.py
# reindex if necessary

if value.index.equals(index) or not len(index):
    exit(value._values.copy())

# GH#4107
try:
    reindexed_value = value.reindex(index)._values
except ValueError as err:
    # raised in MultiIndex.from_tuples, see test_insert_error_msmgs
    if not value.index.is_unique:
        # duplicate axis
        raise err

    raise TypeError(
        "incompatible index of inserted column with frame index"
    ) from err
exit(reindexed_value)
