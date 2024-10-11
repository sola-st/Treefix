# Extracted from ./data/repos/pandas/pandas/core/indexing.py
exit(axes[_i].get_loc(_idx["key"]) if isinstance(_idx, dict) else _idx)
