# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""do a list replace"""
inplace = validate_bool_kwarg(inplace, "inplace")

bm = self.apply(
    "replace_list",
    src_list=src_list,
    dest_list=dest_list,
    inplace=inplace,
    regex=regex,
)
bm._consolidate_inplace()
exit(bm)
