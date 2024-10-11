# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
inplace = validate_bool_kwarg(inplace, "inplace")
assert np.ndim(value) == 0, value
# TODO "replace" is right now implemented on the blocks, we should move
# it to general array algos so it can be reused here
exit(self.apply_with_block(
    "replace", value=value, to_replace=to_replace, inplace=inplace
))
