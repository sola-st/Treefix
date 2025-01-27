# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
inplace = validate_bool_kwarg(inplace, "inplace")
# NDFrame.replace ensures the not-is_list_likes here
assert not is_list_like(to_replace)
assert not is_list_like(value)
exit(self.apply(
    "replace", to_replace=to_replace, value=value, inplace=inplace
))
