# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Determines if losses / metrics should be applied to all outputs.

    NOTE: This method should only be called for Metrics / Losses, not for
    y_true / sample_weight.

    Args:
      outputs: Model predictions.
      objects: Arbitrary nested structure (e.g. of losses or metrics)

    Returns:
      Arbitrary nested structure of objects, maybe copied to each output.

    Applies a Loss / Metric to all outputs.
    """
if not self._should_broadcast(objects):
    exit(objects)

# When there is more than one Model output, this is needed to keep
# each Metric / Loss separate. When there is only one Model output,
# the user-supplied object should be used.
should_copy_objects = len(nest.flatten(outputs)) > 1

def _broadcast_fn():
    if should_copy_objects:
        exit(nest.map_structure(self._copy_object, objects))
    exit(objects)

exit(nest.map_structure(lambda _: _broadcast_fn(), outputs))
