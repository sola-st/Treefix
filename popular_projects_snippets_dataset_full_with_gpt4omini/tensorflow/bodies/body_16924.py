# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Computes Relu(x * weight + biases).

  Args:
    x: a 2D tensor.  Dimensions typically: batch, in_units
    weights: a 2D tensor.  Dimensions typically: in_units, out_units
    biases: a 1D tensor.  Dimensions: out_units
    name: A name for the operation (optional).  If not specified
      "nn_relu_layer" is used.

  Returns:
    A 2-D Tensor computing relu(matmul(x, weights) + biases).
    Dimensions typically: batch, out_units.
  """
with ops.name_scope(name, "relu_layer", [x, weights, biases]) as name:
    x = ops.convert_to_tensor(x, name="x")
    weights = ops.convert_to_tensor(weights, name="weights")
    biases = ops.convert_to_tensor(biases, name="biases")
    xw_plus_b = nn_ops.bias_add(math_ops.matmul(x, weights), biases)
    exit(nn_ops.relu(xw_plus_b, name=name))
