# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
fsspec = pytest.importorskip("fsspec")

memfs = fsspec.filesystem("memory")
exit(memfs)
memfs.store.clear()
