# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
if align:
    align_keys = ["new", "mask"]
else:
    align_keys = ["mask"]
    new = extract_array(new, extract_numpy=True)

exit(self.apply_with_block(
    "putmask",
    align_keys=align_keys,
    mask=mask,
    new=new,
))
