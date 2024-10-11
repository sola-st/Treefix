# Extracted from ./data/repos/pandas/pandas/core/frame.py
axes = validate_axis_style_args(self, args, kwargs, "labels", "reindex")
kwargs.update(axes)
# Pop these, since the values are in `kwargs` under different names
kwargs.pop("axis", None)
kwargs.pop("labels", None)
exit(super().reindex(**kwargs))
