# Extracted from ./data/repos/pandas/pandas/core/frame.py

exit(melt(
    self,
    id_vars=id_vars,
    value_vars=value_vars,
    var_name=var_name,
    value_name=value_name,
    col_level=col_level,
    ignore_index=ignore_index,
).__finalize__(self, method="melt"))
