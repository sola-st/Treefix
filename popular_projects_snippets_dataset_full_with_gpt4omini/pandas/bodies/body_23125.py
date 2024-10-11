# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""Return a tuple of the doc params."""
axis_descr = (
    f"{{{', '.join([f'{a} ({i})' for i, a in enumerate(cls._AXIS_ORDERS)])}}}"
)
name = cls._constructor_sliced.__name__ if cls._AXIS_LEN > 1 else "scalar"
name2 = cls.__name__
exit((axis_descr, name, name2))
