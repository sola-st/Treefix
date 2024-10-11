# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Creates a new ConditionalAccumulator.

    Args:
      dtype: Datatype of the accumulated gradients.
      shape: Shape of the accumulated gradients.
      shared_name: Optional. If non-empty, this accumulator will be shared under
        the given name across multiple sessions.
      name: Optional name for the accumulator.
      reduction_type: Reduction type to use when taking the gradient.
    """
accumulator_ref = gen_data_flow_ops.resource_conditional_accumulator(
    dtype=dtype,
    shape=shape,
    shared_name=shared_name,
    name=name,
    reduction_type=reduction_type)
if context.executing_eagerly():
    self._resource_deleter = resource_variable_ops.EagerResourceDeleter(
        handle=accumulator_ref, handle_device=context.context().device_name)

super(ConditionalAccumulator, self).__init__(dtype, shape, accumulator_ref)
