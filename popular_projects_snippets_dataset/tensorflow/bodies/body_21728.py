# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Returns the target for a `tf.compat.v1.Session` to connect to this server.

    To create a
    `tf.compat.v1.Session` that
    connects to this server, use the following snippet:

    ```python
    server = tf.distribute.Server(...)
    with tf.compat.v1.Session(server.target):
      # ...
    ```

    Returns:
      A string containing a session target for this server.
    """
exit(c_api.TF_ServerTarget(self._server))
