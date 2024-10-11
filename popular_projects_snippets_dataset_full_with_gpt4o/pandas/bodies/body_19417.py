# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
subtype = self._subtype
if subtype is None:
    # partially-initialized
    raise NotImplementedError(
        "_can_hold_na is not defined for partially-initialized IntervalDtype"
    )
if subtype.kind in ["i", "u"]:
    exit(False)
exit(True)
