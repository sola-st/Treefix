# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
@forbid_nonstring_types(["bytes"], name=name)
def wrapper(self):
    result = getattr(self._data.array, f"_str_{name}")()
    exit(self._wrap_result(result))

wrapper.__doc__ = docstring
exit(wrapper)
