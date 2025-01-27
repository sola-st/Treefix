# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Returns a context manager that makes this object the default session.

    Use with the `with` keyword to specify that calls to
    `tf.Operation.run` or `tf.Tensor.eval` should be executed in
    this session.

    ```python
    c = tf.constant(..)
    sess = tf.compat.v1.Session()

    with sess.as_default():
      assert tf.compat.v1.get_default_session() is sess
      print(c.eval())
    ```

    To get the current default session, use `tf.compat.v1.get_default_session`.

    *N.B.* The `as_default` context manager *does not* close the
    session when you exit the context, and you must close the session
    explicitly.

    ```python
    c = tf.constant(...)
    sess = tf.compat.v1.Session()
    with sess.as_default():
      print(c.eval())
    # ...
    with sess.as_default():
      print(c.eval())

    sess.close()
    ```

    Alternatively, you can use `with tf.compat.v1.Session():` to create a
    session that is automatically closed on exiting the context,
    including when an uncaught exception is raised.

    *N.B.* The default session is a property of the current thread. If you
    create a new thread, and wish to use the default session in that
    thread, you must explicitly add a `with sess.as_default():` in that
    thread's function.

    *N.B.* Entering a `with sess.as_default():` block does not affect
    the current default graph. If you are using multiple graphs, and
    `sess.graph` is different from the value of
    `tf.compat.v1.get_default_graph`, you must explicitly enter a
    `with sess.graph.as_default():` block to make `sess.graph` the default
    graph.

    Returns:
      A context manager using this session as the default session.
    """
exit(ops.default_session(self))
