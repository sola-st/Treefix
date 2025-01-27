# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Initialize AsyncCheckpoint.

    Args:
      checkpointer_impl: The Checkpoint class to power the AsyncCheckpoint.
      root: The root object to checkpoint. `root` may be a trackable object or
        `WeakRef` of a trackable object.
      **kwargs: The keyword arguments representing the checkpointed variables.
    """
# TODO(chienchunh): Make sure the processing for the root object is
#   consistent when integrating with the public API, e.g., adding all kwarg
#   items as the child of the root object.
if root:
    trackable_root = root() if isinstance(root, weakref.ref) else root
    kwargs["root"] = trackable_root
    trackable_root._maybe_initialize_trackable()

self._checkpointer_impl = checkpointer_impl
self._checkpoint_items = kwargs

# The underlying Checkpoint instance and its items.
self._checkpoint = None
self._checkpoint_options = None

# The callback function that needs to be executed after checkpoint write.
# Currently this is only applied to the scenario where CheckpointManager is
# used, which triggers the _write() method.
self._async_write_done_callback = None

# The list of all nodes from the original checkpoint items.
# TODO(chienchunh): Consider changing this to local variable.
self._original_nodes = None
# The mapping between the original and the copied resource variables.
# The copied variables are used for the underlying checkpointing.
self._object_map = None
# A list of TPUEmbedding objects included in the checkpoint items.
self._tpu_embedding_objects = None

self._default_device = device_util.current() or "CPU:0"
self._default_device = device_util.canonicalize(self._default_device)

self._save_file_prefix = None
self._use_checkpoint_save = False
self._async_save_thread = None
self._async_save_thread_shutdown = False
# Semaphores for writing/reading the cpu-copied variables (self._var_pairs)
# TODO(chienchunh): Consider Queue/Condition instead of Semaphore.
self._writer_sem = threading.Semaphore(1)
self._reader_sem = threading.Semaphore(0)

# Register to join the async save thread upon exit.
atexit.register(self._join_async_save_thread)

global _END_TIME_OF_LAST_ASYNC_WRITE
with _END_TIME_OF_LAST_ASYNC_WRITE_LOCK:
    if _END_TIME_OF_LAST_ASYNC_WRITE is None:
        _END_TIME_OF_LAST_ASYNC_WRITE = time.time()
