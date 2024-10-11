# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Initialize the async checkpoint internal state."""
if self._checkpoint is not None:
    exit()

self._original_nodes = []
self._object_map = object_identity.ObjectIdentityDictionary()
self._tpu_embedding_objects = []

# Add the top-level checkpoint items to be traversed,
to_traverse = collections.deque([])
visited = object_identity.ObjectIdentitySet()
for v in self._checkpoint_items.values():
    if isinstance(v, (Variable, ShardedVariable)):
        self._copy_trackable(v)
    elif isinstance(v, TPUEmbedding):
        self._handle_tpu_embedding(v)
    to_traverse.append(v)
    visited.add(v)
self._traverse_variables(to_traverse, visited)

# Copy for the slot variables.
for current_trackable in self._original_nodes:
    if (isinstance(current_trackable, optimizer_v1.Optimizer)
        # Note: dir() is used rather than hasattr() here to avoid triggering
        # custom __getattr__ code, see b/152031870 for context.
        or "get_slot_names" in dir(current_trackable)):
        slot_names = current_trackable.get_slot_names()
        for slot_name in slot_names:
            for original_variable in self._original_nodes:
                if not isinstance(original_variable, Variable):
                    continue
                try:
                    original_slot_variable = current_trackable.get_slot(
                        original_variable, slot_name)
                except (AttributeError, KeyError):
                    continue
                if isinstance(original_slot_variable, (Variable, ShardedVariable)):
                    self._copy_trackable(original_slot_variable)

    # Initiate the underlying Checkpoint instance with the copied items.
self._checkpoint = self._checkpointer_impl(**self._checkpoint_items)

# Pass the object map of the copied variables to the underlying Checkpoint.
self._checkpoint._saver._object_map = self._object_map  # pylint: disable=protected-access

# Initiate the async thread for checkpoint saving.
self._async_save_thread = threading.Thread(
    target=self._async_save, daemon=True)
self._async_save_thread.start()
