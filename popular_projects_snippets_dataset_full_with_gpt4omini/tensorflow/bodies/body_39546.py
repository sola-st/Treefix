# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Create a save counter if it does not yet exist."""
if self._save_counter is None:
    # Initialized to 0 and incremented before saving.
    with ops.device("/cpu:0"):
        # add_variable creates a dependency named "save_counter"; NoDependency
        # prevents creating a second dependency named "_save_counter".
        self._save_counter = data_structures.NoDependency(
            add_variable(
                self,
                name="save_counter",
                initializer=0,
                dtype=dtypes.int64,
                trainable=False))
        if self._attached_dependencies is not None:
            self._attached_dependencies.append(
                # Store a stronge reference to the `save_counter`, so that if the
                # `Checkpoint` object is deleted, the `save_counter` does not get
                # deleted immediately. (The LoadStatus object needs to indirectly
                # reference the counter through the ObjectGraphView).
                base.TrackableReference("save_counter", self._save_counter))
            # When loading a checkpoint, the save counter is created after
            # the checkpoint has been loaded, so it must be handled in a deferred
            # manner.
            if isinstance(self.root, weakref.ref):
                root = self.root()
            else:
                root = self.root
            restore = root._deferred_dependencies.pop("save_counter", ())  # pylint: disable=protected-access
            if restore:
                restore[0].restore(self._save_counter)
