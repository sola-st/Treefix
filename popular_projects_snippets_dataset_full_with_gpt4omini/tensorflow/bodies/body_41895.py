# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Given outputs from the execution of `forward`, records the operation."""
if (self._tape_watching
    and not isinstance(flat_outputs, ops.Operation)
    and flat_outputs is not None):
    # We only record function calls which have outputs, and then only when a
    # tape is watching.
    self._functions.record(
        flat_outputs, self._inference_args, self._input_tangents)
