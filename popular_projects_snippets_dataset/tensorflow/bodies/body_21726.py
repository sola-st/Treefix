# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Blocks until the server has shut down.

    This method currently blocks forever.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        joining the TensorFlow server.
    """
c_api.TF_ServerJoin(self._server)
