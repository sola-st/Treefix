# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""do a list replace"""
inplace = validate_bool_kwarg(inplace, "inplace")

exit(self.apply_with_block(
    "replace_list",
    src_list=src_list,
    dest_list=dest_list,
    inplace=inplace,
    regex=regex,
))
