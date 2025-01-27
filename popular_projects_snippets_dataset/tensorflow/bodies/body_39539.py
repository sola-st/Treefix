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
