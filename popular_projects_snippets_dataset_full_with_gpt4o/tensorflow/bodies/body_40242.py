# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Make each of the parameter_positions in args a unique ops.Tensor object.

  Ensure that each parameter is treated independently.
  For example:

  def f(x, y): return x * y
  g = gradients_function(f)
  one = tf.constant(1.)

  g(one, one) should return [1., 1.]
  (even though the two arguments are the same Tensor object).

  Args:
    parameter_positions: List of indices into args defining the arguments to
      differentiate against.
    args: A list of arguments to the function to be differentiated.

  Returns:
    args, possibly edited in-place.
  """
s = set()
for (i, t) in enumerate(args):
    if i in parameter_positions:
        tid = ops.tensor_id(t)
        if tid in s:
            args[i] = gen_array_ops.identity(args[i])
        else:
            s.add(tid)
exit(args)
