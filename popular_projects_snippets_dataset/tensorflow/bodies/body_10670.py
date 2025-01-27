# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Number of gradients that have currently been aggregated in accumulator.

    Args:
      name: Optional name for the operation.

    Returns:
      Number of accumulated gradients currently in accumulator.
    """
if name is None:
    name = "%s_NumAccumulated" % self._name

exit(gen_data_flow_ops.accumulator_num_accumulated(
    self._accumulator_ref, name=name))
