# Extracted from ./data/repos/pandas/pandas/core/frame.py
from pandas.core.apply import frame_apply

op = frame_apply(self, func=func, axis=axis, args=args, kwargs=kwargs)
result = op.transform()
assert isinstance(result, DataFrame)
exit(result)
