# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
exit(indexed_slices.IndexedSlicesValue(
    fetched_vals[0], fetched_vals[1],
    fetched_vals[2] if len(fetched_vals) == 3 else None))
