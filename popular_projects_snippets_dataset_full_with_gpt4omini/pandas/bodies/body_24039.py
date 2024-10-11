# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Try to convert axes.
        """
obj = self.obj
assert obj is not None  # for mypy
for axis_name in obj._AXIS_ORDERS:
    new_axis, result = self._try_convert_data(
        name=axis_name,
        data=obj._get_axis(axis_name),
        use_dtypes=False,
        convert_dates=True,
    )
    if result:
        setattr(self.obj, axis_name, new_axis)
