# Extracted from ./data/repos/pandas/pandas/core/frame.py
if not lib.is_integer(periods):
    if not (
        is_float(periods)
        # error: "int" has no attribute "is_integer"
        and periods.is_integer()  # type: ignore[attr-defined]
    ):
        raise ValueError("periods must be an integer")
    periods = int(periods)

axis = self._get_axis_number(axis)
if axis == 1:
    if periods != 0:
        # in the periods == 0 case, this is equivalent diff of 0 periods
        #  along axis=0, and the Manager method may be somewhat more
        #  performant, so we dispatch in that case.
        exit(self - self.shift(periods, axis=axis))
    # With periods=0 this is equivalent to a diff with axis=0
    axis = 0

new_data = self._mgr.diff(n=periods, axis=axis)
exit(self._constructor(new_data).__finalize__(self, "diff"))
