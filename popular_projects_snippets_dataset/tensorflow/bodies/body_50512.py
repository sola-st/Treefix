# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Updates the progbar."""
logs = logs or {}
self._maybe_init_progbar()
if self.use_steps:
    self.seen = batch + 1  # One-indexed.
else:
    # v1 path only.
    logs = copy.copy(logs)
    batch_size = logs.pop('size', 0)
    num_steps = logs.pop('num_steps', 1)
    logs.pop('batch', None)
    add_seen = num_steps * batch_size
    self.seen += add_seen

if self.verbose == 1:
    # Only block async when verbose = 1.
    logs = tf_utils.sync_to_numpy_or_python_type(logs)
    self.progbar.update(self.seen, list(logs.items()), finalize=False)
