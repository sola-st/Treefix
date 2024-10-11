# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
if align:
    align_keys = ["other", "cond"]
else:
    align_keys = ["cond"]
    other = extract_array(other, extract_numpy=True)

exit(self.apply_with_block(
    "where",
    align_keys=align_keys,
    other=other,
    cond=cond,
))
