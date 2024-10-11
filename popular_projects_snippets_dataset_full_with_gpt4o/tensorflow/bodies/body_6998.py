# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Set `output` with `name` to be captured as a non tensor output."""
if distribution_strategy_context.in_cross_replica_context():
    self._non_tensor_outputs[name] = output
else:
    def merge_fn(distribution, value):
        # NOTE(priyag): For non tensor outputs, we simply return all the values
        # in a list as reduction doesn't make sense on non tensors.
        self._non_tensor_outputs[name] = (
            distribution.experimental_local_results(value))
    distribution_strategy_context.get_replica_context().merge_call(
        merge_fn, args=(output,))
