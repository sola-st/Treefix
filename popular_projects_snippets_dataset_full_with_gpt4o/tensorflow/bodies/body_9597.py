# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Allocate fake process ids for each device in the StepStats."""
self._allocators_pid = self._alloc_pid()
self._chrome_trace.emit_pid('Allocators', self._allocators_pid)

# Add processes in the Chrome trace to show compute and data activity.
for dev_stats in self._step_stats.dev_stats:
    device_pid = self._alloc_pid()
    self._device_pids[dev_stats.device] = device_pid
    tensors_pid = self._alloc_pid()
    self._tensor_pids[dev_stats.device] = tensors_pid
    self._chrome_trace.emit_pid(dev_stats.device + ' Compute', device_pid)
    self._chrome_trace.emit_pid(dev_stats.device + ' Tensors', tensors_pid)
