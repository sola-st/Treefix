# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns True if current thread has eager executing enabled."""
exit(self._thread_local_data.is_eager)
