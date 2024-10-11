# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
if context.executing_eagerly():
    raise RuntimeError("Use save/restore instead of build in eager mode.")
self._build(self._filename, build_save=True, build_restore=True)
