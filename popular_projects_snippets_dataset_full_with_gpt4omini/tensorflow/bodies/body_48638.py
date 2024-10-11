# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# TODO(b/152094471): Support this with DistIter.get_next_as_optional.
if self._steps_per_execution_value > 1 and self._inferred_steps is None:
    raise ValueError(
        "Could not infer the size of the data. With "
        "`steps_per_execution > 1`, you must specify the number of steps "
        "to run.")
