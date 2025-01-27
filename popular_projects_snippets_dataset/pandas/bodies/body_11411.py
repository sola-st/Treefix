# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
with open(path, "wb") as fh:
    pickle.dump(obj, fh, protocol=-1)
