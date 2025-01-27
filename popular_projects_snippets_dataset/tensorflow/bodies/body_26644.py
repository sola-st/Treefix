# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
"""Returns a target that can be used to connect to the server.

    >>> dispatcher = tf.data.experimental.service.DispatchServer()
    >>> dataset = tf.data.Dataset.range(10)
    >>> dataset = dataset.apply(tf.data.experimental.service.distribute(
    ...     processing_mode="parallel_epochs", service=dispatcher.target))

    The returned string will be in the form protocol://address, e.g.
    "grpc://localhost:5050".
    """
exit("{0}://localhost:{1}".format(self._config.protocol,
                                    self._server.bound_port()))
