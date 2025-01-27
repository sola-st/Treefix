# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Creates a new ConditionalAccumulator.

    Args:
      dtype: Datatype of the accumulated gradients.
      shape: Shape of the accumulated gradients.
      accumulator_ref: A handle to the conditional accumulator, created by sub-
        classes
    """
self._dtype = dtype
if shape is not None:
    self._shape = tensor_shape.TensorShape(shape)
else:
    self._shape = tensor_shape.unknown_shape()
self._accumulator_ref = accumulator_ref
if context.executing_eagerly():
    self._name = context.context().scope_name
else:
    self._name = self._accumulator_ref.op.name.split("/")[-1]
