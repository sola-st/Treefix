# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_cache.py
"""Clear cached summary writers. Currently only used for unit tests."""
with FileWriterCache._lock:
    # Make sure all the writers are closed now (otherwise open file handles
    # may hang around, blocking deletions on Windows).
    for item in FileWriterCache._cache.values():
        item.close()
    FileWriterCache._cache = {}
