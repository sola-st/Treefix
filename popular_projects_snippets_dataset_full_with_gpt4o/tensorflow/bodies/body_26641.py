# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
"""Starts this server.

    >>> dispatcher = tf.data.experimental.service.DispatchServer(start=False)
    >>> dispatcher.start()

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        starting the server.
    """
self._server.start()
