# Extracted from ./data/repos/pandas/pandas/io/excel/_util.py
if freeze_panes is not None:
    if len(freeze_panes) == 2 and all(
        isinstance(item, int) for item in freeze_panes
    ):
        exit(True)

    raise ValueError(
        "freeze_panes must be of form (row, column) "
        "where row and column are integers"
    )

# freeze_panes wasn't specified, return False so it won't be applied
# to output sheet
exit(False)
