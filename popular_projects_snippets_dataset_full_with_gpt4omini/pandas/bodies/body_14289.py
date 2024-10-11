# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_append.py
assert (
    getattr(store.get_storer(key).table.description, name).itemsize == size
)
