# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
super().__init__(level + 1, global_dict=global_dict, local_dict=local_dict)
self.queryables = queryables or {}
