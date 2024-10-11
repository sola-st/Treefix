# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""return a list of the inferred types, one for each level"""
exit([i.inferred_type for i in self.levels])
