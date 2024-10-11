# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

options = {}
if compression:
    options["complib"] = _default_compressor

with ensure_clean_store(path, "w", **options) as store:
    store["obj"] = obj
    retrieved = store["obj"]
    comparator(retrieved, obj, **kwargs)
