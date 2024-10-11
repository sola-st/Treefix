# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Group objects into a training checkpoint.

    Args:
      **kwargs: Keyword arguments are set as attributes of this object, and are
        saved with the checkpoint. Values must be trackable objects.

    Raises:
      ValueError: If objects in `kwargs` are not trackable.
    """
super().__init__()
global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    if _END_TIME_OF_LAST_WRITE is None:
        _END_TIME_OF_LAST_WRITE = time.time()

for k, v in sorted(kwargs.items(), key=lambda item: item[0]):
    setattr(self, k, v)
    if not isinstance(
        getattr(self, k), (base.Trackable, def_function.Function)):
        raise ValueError(
            "`Checkpoint` was expecting a trackable object (an object "
            f"derived from `Trackable`), got {v}. If you believe this "
            "object should be trackable (i.e. it is part of the "
            "TensorFlow Python API and manages state), please open an issue.")
self._save_counter = None  # Created lazily for restore-on-create.
self._save_assign_op = None
self._saver = TrackableSaver(graph_view_lib.ObjectGraphView(self))
