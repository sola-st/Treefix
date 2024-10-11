# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
self.restore_ops.extend(new_ops)
if self.new_restore_ops_callback:
    self.new_restore_ops_callback(new_ops)  # pylint: disable=not-callable
