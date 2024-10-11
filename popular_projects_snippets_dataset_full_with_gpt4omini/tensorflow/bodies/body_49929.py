# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/legacy_learning_rate_decay.py
"""Applies natural exponential decay to the initial learning rate.

  When training a model, it is often recommended to lower the learning rate as
  the training progresses.  This function applies an exponential decay function
  to a provided initial learning rate.  It requires an `global_step` value to
  compute the decayed learning rate.  You can just pass a TensorFlow variable
  that you increment at each training step.

  The function returns the decayed learning rate.  It is computed as:

  ```python
  decayed_learning_rate = learning_rate * exp(-decay_rate * global_step /
  decay_step)
  ```

  or, if `staircase` is `True`, as:

  ```python
  decayed_learning_rate = learning_rate * exp(-decay_rate * floor(global_step /
  decay_step))
  ```

  Example: decay exponentially with a base of 0.96:

  ```python
  ...
  global_step = tf.Variable(0, trainable=False)
  learning_rate = 0.1
  decay_steps = 5
  k = 0.5
  learning_rate = tf.compat.v1.train.natural_exp_decay(learning_rate,
  global_step,
                                             decay_steps, k)

  # Passing global_step to minimize() will increment it at each step.
  learning_step = (
      tf.compat.v1.train.GradientDescentOptimizer(learning_rate)
      .minimize(...my loss..., global_step=global_step)
  )
  ```

  Args:
    learning_rate: A scalar `float32` or `float64` `Tensor` or a Python number.
      The initial learning rate.
    global_step: A Python number. Global step to use for the decay computation.
      Must not be negative.
    decay_steps: How often to apply decay.
    decay_rate: A Python number.  The decay rate.
    staircase: Whether to apply decay in a discrete staircase, as opposed to
      continuous, fashion.
    name: String.  Optional name of the operation.  Defaults to
      'ExponentialTimeDecay'.

  Returns:
    A scalar `Tensor` of the same type as `learning_rate`.  The decayed
    learning rate.

  Raises:
    ValueError: if `global_step` is not supplied.

  @compatibility(eager)
  When eager execution is enabled, this function returns a function which in
  turn returns the decayed learning rate Tensor. This can be useful for changing
  the learning rate value across different invocations of optimizer functions.
  @end_compatibility
  """
natural_exp_rate = math_ops.exp(math_ops.negative(decay_rate))
decayed_lr = learning_rate_schedule.ExponentialDecay(
    learning_rate,
    decay_steps,
    natural_exp_rate,
    staircase=staircase,
    name=name)

if not context.executing_eagerly():
    decayed_lr = decayed_lr(global_step)
else:
    decayed_lr = functools.partial(decayed_lr, global_step)
exit(decayed_lr)
