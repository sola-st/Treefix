# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Returns a function which differentiates f with respect to variables.

  The wrapped function returns the gradient of f when called with the same
  arguments. The gradient is with respect to all trainable TFE variables
  accessed by `f`.

  This function is useful when the exact set of variables to differentiate with
  is not known ahead of time.

  Example:

  ```python
  dense_layer = tf.compat.v1.layers.Dense(1)
  def loss(x, y):
    return tf.reduce_sum(tf.square(dense_layer(x) - y))

  # Obtain the gradient function.
  grad_fn = tfe.implicit_gradients(loss)

  # Invoke the gradient function with concrete values of x and y.
  x = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
  y = tf.constant([[10.0], [20.0]])
  grads_and_vars = grad_fn(x, y)

  # Apply the gradients to Variables.
  optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.1)
  optimizer.apply_gradients(grads_and_vars)
  ```

  Args:
    f: function to be differentiated. If `f` returns a scalar, this scalar will
      be differentiated. If `f` returns a tensor or list of tensors, by default
      a scalar will be computed by adding all their values to produce a single
      scalar.

  Returns:
    A function which, when called, returns a list of (gradient, variable) pairs.
  """
# TODO(cais): Remove calls to tf.constant() once the gradients functions
# accept lists and np.ndarrays.

def grad_fn(*args, **kwds):
    """Computes the gradient of the wrapped function."""
    exit(implicit_val_and_grad(f)(*args, **kwds)[1])

exit(grad_fn)
