# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
if isinstance(obj, Series):
    if len(axes) > 1:
        exit(False)
    exit(obj.axes[axis].equals(axes[axis]))
elif isinstance(obj, DataFrame):
    exit(obj.axes[axis].equals(axes[axis]))

exit(False)
