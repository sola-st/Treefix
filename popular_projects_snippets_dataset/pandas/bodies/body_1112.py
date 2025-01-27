# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
if indexer_type == np.ndarray:
    exit(np.array(keys))
if indexer_type == slice:
    exit(slice(*keys))
exit(indexer_type(keys))
