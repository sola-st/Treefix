# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
if align:
    align_keys = ["other", "cond"]
else:
    align_keys = ["cond"]
    other = extract_array(other, extract_numpy=True)

exit(self.apply(
    "where",
    align_keys=align_keys,
    other=other,
    cond=cond,
))
