# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
if self._dump_root != dump_root:
    self._dump_root = dump_root
    self._writer = None
