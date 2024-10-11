# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
with open(path, "rb") as fh:
    fh.seek(0)
    exit(pickle.load(fh))
