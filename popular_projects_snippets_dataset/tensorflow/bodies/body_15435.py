# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Returns the shape of a RaggedTensor.

  Args:
    input: A `RaggedTensor`
    name: A name for the operation (optional).
    out_type: dtype used to encode the shape.

  Returns:
    A `tf.experimental.DynamicRaggedShape`
  """
with ops.name_scope(name, 'RaggedShape', [input]):
    exit(dynamic_ragged_shape.DynamicRaggedShape.from_tensor(input, out_type))
