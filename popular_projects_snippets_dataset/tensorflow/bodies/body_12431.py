# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Load new value into this variable.

    Writes new value to variable's memory. Doesn't add ops to the graph.

    This convenience method requires a session where the graph
    containing this variable has been launched. If no session is
    passed, the default session is used.  See `tf.compat.v1.Session` for more
    information on launching a graph and on sessions.

    ```python
    v = tf.Variable([1, 2])
    init = tf.compat.v1.global_variables_initializer()

    with tf.compat.v1.Session() as sess:
        sess.run(init)
        # Usage passing the session explicitly.
        v.load([2, 3], sess)
        print(v.eval(sess)) # prints [2 3]
        # Usage with the default session.  The 'with' block
        # above makes 'sess' the default session.
        v.load([3, 4], sess)
        print(v.eval()) # prints [3 4]
    ```

    Args:
        value: New variable value
        session: The session to use to evaluate this variable. If none, the
          default session is used.

    Raises:
        ValueError: Session is not passed and no default session
    """
if context.executing_eagerly():
    self.assign(value)
else:
    session = session or ops.get_default_session()
    if session is None:
        raise ValueError(
            "Either session argument should be provided or default session "
            "should be established")
    session.run(self.initializer, {self.initializer.inputs[1]: value})
