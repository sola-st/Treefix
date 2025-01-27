# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients.py
"""Computes and stacks jacobians of `output[i,...]` w.r.t. `input[i,...]`.

  e.g.
  x = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
  y = x * x
  jacobian = batch_jacobian(y, x)
  # => [[[2,  0], [0,  4]], [[6,  0], [0,  8]]]

  Args:
    output: A tensor with shape [b, y1, ..., y_n]. `output[i,...]` should
      only depend on `inp[i,...]`.
    inp: A tensor with shape [b, x1, ..., x_m]
    use_pfor: If true, uses pfor for computing the Jacobian. Else uses a
      tf.while_loop.
    parallel_iterations: A knob to control how many iterations are vectorized
      and dispatched in parallel. The default value of None, when use_pfor is
      true, corresponds to vectorizing all the iterations. When use_pfor is
      false, the default value of None corresponds to parallel_iterations=10.
      This knob can be used to control the total memory usage.

  Returns:
    A tensor `t` with shape [b, y_1, ..., y_n, x1, ..., x_m] where `t[i, ...]`
    is the jacobian of `output[i, ...]` w.r.t. `inp[i, ...]`, i.e. stacked
    per-example jacobians.

  Raises:
    ValueError: if first dimension of `output` and `inp` do not match.
  """
output_shape = output.shape
if not output_shape[0].is_compatible_with(inp.shape[0]):
    raise ValueError(f"Need first dimension of `output` shape ({output.shape}) "
                     f"and `inp` shape ({inp.shape}) to match.")
if output_shape.is_fully_defined():
    batch_size = int(output_shape[0])
    output_row_size = output_shape.num_elements() // batch_size
else:
    output_shape = array_ops.shape(output)
    batch_size = output_shape[0]
    output_row_size = array_ops.size(output) // batch_size
inp_shape = array_ops.shape(inp)
# Flatten output to 2-D.
with ops.control_dependencies(
    [check_ops.assert_equal(batch_size, inp_shape[0])]):
    output = array_ops.reshape(output, [batch_size, output_row_size])

def loop_fn(i):
    y = array_ops.gather(output, i, axis=1)
    exit(gradient_ops.gradients(y, inp)[0])

if use_pfor:
    pfor_output = control_flow_ops.pfor(loop_fn, output_row_size,
                                        parallel_iterations=parallel_iterations)
else:
    pfor_output = control_flow_ops.for_loop(
        loop_fn, output.dtype,
        output_row_size,
        parallel_iterations=parallel_iterations)
if pfor_output is None:
    exit(None)
pfor_output = array_ops.reshape(pfor_output,
                                [output_row_size, batch_size, -1])
output = array_ops.transpose(pfor_output, [1, 0, 2])
new_shape = array_ops.concat([output_shape, inp_shape[1:]], axis=0)
exit(array_ops.reshape(output, new_shape))
