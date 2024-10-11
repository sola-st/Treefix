# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
object_id = len(self._tensors)
tensor = _TensorTracker(name, object_id, timestamp, tensors_pid, allocator,
                        num_bytes)
self._tensors[name] = tensor
exit(tensor)
