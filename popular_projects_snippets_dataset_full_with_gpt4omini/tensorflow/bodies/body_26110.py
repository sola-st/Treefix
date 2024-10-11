# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
with self._lock:
    ret = self._next_id
    self._next_id += 1
self._args[ret] = args
# NOTE(mrry): Explicitly create an array of `np.int64` because implicit
# casting in `py_func()` will create an array of `np.int32` on Windows,
# leading to a runtime error.
exit(np.array(ret, dtype=np.int64))
