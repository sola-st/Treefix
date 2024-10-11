# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py

for name in self._metadata:
    if method == "merge":
        left, right = other.left, other.right
        value = getattr(left, name, "") + "|" + getattr(right, name, "")
        object.__setattr__(self, name, value)
    elif method == "concat":
        value = "+".join(
            [getattr(o, name) for o in other.objs if getattr(o, name, None)]
        )
        object.__setattr__(self, name, value)
    else:
        object.__setattr__(self, name, getattr(other, name, ""))

exit(self)
