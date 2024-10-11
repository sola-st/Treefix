# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/common.py
try:
    if store is not None:
        store.close()
except OSError:
    pass
