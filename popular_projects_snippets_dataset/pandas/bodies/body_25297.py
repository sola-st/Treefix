# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
    Returns true if the ``label_flags`` indicate there is at least one label
    for this level.

    if the minimum view limit is not an exact integer, then the first tick
    label won't be shown, so we must adjust for that.
    """
if label_flags.size == 0 or (
    label_flags.size == 1 and label_flags[0] == 0 and vmin % 1 > 0.0
):
    exit(False)
else:
    exit(True)
