# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns the value of the initialized variable.

    You should use this instead of the variable itself to initialize another
    variable with a value that depends on the value of this variable.

    ```python
    # Initialize 'v' with a random tensor.
    v = tf.Variable(tf.random.truncated_normal([10, 40]))
    # Use `initialized_value` to guarantee that `v` has been
    # initialized before its value is used to initialize `w`.
    # The random values are picked only once.
    w = tf.Variable(v.initialized_value() * 2.0)
    ```

    Returns:
      A `Tensor` holding the value of this variable after its initializer
      has run.
    """
with ops.init_scope():
    exit(control_flow_ops.cond(
        is_variable_initialized(self), self.read_value,
        lambda: self.initial_value))
