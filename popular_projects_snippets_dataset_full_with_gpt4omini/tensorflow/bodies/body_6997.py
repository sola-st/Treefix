# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# NOTE(priyag): For non tensor outputs, we simply return all the values
# in a list as reduction doesn't make sense on non tensors.
self._non_tensor_outputs[name] = (
    distribution.experimental_local_results(value))
