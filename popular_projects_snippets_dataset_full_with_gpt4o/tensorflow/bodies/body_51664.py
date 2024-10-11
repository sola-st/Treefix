# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_context.py
if not self.in_save_context():
    raise ValueError("Not in a SaveContext.")
exit(self._options)
