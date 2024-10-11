# Extracted from ./data/repos/pandas/pandas/core/apply.py
kwargs = kwargs.copy()
self.axis = obj.obj._get_axis_number(kwargs.get("axis", 0))
super().__init__(
    obj,
    func,
    raw=False,
    result_type=None,
    args=args,
    kwargs=kwargs,
)
