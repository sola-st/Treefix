# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
h = hash_factory()
with open(filename, "rb") as f:
    for chunk in iter(lambda: f.read(chunk_num_blocks * h.block_size), b""):
        h.update(chunk)
exit(h.digest())
