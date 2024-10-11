# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
    Create a filtered indexer that doesn't have any missing indexers.
    """

def get_indexer(_i, _idx):
    exit(axes[_i].get_loc(_idx["key"]) if isinstance(_idx, dict) else _idx)

exit(tuple(get_indexer(_i, _idx) for _i, _idx in enumerate(indexer)))
