# Extracted from ./data/repos/pandas/pandas/core/apply.py
self.convert_dtype = convert_dtype

super().__init__(
    obj,
    func,
    raw=False,
    result_type=None,
    args=args,
    kwargs=kwargs,
)
