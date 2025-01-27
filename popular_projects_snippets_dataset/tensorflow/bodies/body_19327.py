# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/matmul_benchmark.py
"""Build a graph containing a sequence of matmul operations.

  Args:
    device: String, the device to run on.
    n: tensor A's first dimension size.
    m: tensor A's second dimension size.
    k: tensor B's second dimension size.
    transpose_a: boolean value to show if tensor A is transposed.
    transpose_b: boolean value to show if tensor B is transposed.
    dtype: numpy data type of the input tensor.

  Returns:
    A matmul operation to run()
  """
with ops.device('%s' % device):
    if not transpose_a:
        x = variables.VariableV1(random_ops.random_uniform([n, m], dtype=dtype),
                                 use_resource=False)
    else:
        x = variables.VariableV1(random_ops.random_uniform([m, n], dtype=dtype),
                                 use_resource=False)
    if not transpose_b:
        y = variables.VariableV1(random_ops.random_uniform([m, k], dtype=dtype),
                                 use_resource=False)
    else:
        y = variables.VariableV1(random_ops.random_uniform([k, m], dtype=dtype),
                                 use_resource=False)

    z = math_ops.matmul(x, y, transpose_a=transpose_a, transpose_b=transpose_b)
    exit(control_flow_ops.group(z))
