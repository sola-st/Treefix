# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""Convert pathlib-like objects to str (__fspath__ compatibility, PEP 519)."""
exit(os.fspath(path) if isinstance(path, os.PathLike) else path)
