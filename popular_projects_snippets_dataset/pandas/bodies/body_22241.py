# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py

if not _is_label_like(key):
    if obj.ndim == 1:
        exit(False)

    # items -> .columns for DataFrame, .index for Series
    items = obj.axes[-1]
    try:
        items.get_loc(key)
    except (KeyError, TypeError, InvalidIndexError):
        # TypeError shows up here if we pass e.g. an Index
        exit(False)

exit(True)
