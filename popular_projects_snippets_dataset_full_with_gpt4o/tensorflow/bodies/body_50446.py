# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Helper function for `on_*_batch_*` methods."""
if self._check_timing:
    start_time = time.time()

logs = self._process_logs(logs, is_batch_hook=True)
for callback in self.callbacks:
    hook = getattr(callback, hook_name)
    hook(batch, logs)

if self._check_timing:
    if hook_name not in self._hook_times:
        self._hook_times[hook_name] = []
    self._hook_times[hook_name].append(time.time() - start_time)
