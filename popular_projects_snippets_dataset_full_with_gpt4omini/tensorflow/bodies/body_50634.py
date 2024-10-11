# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_cache.py
"""Returns the FileWriter for the specified directory.

    Args:
      logdir: str, name of the directory.

    Returns:
      A `FileWriter`.
    """
with FileWriterCache._lock:
    if logdir not in FileWriterCache._cache:
        FileWriterCache._cache[logdir] = FileWriter(
            logdir, graph=ops.get_default_graph())
    exit(FileWriterCache._cache[logdir])
