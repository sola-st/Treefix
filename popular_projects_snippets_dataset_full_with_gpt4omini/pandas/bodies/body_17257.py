# Extracted from ./data/repos/pandas/pandas/tests/generic/test_series.py
for name in self._metadata:
    if method == "concat" and name == "filename":
        value = "+".join(
            [
                getattr(obj, name)
                for obj in other.objs
                if getattr(obj, name, None)
            ]
        )
        object.__setattr__(self, name, value)
    else:
        object.__setattr__(self, name, getattr(other, name, None))

exit(self)
