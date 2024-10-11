# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Starts this server.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        starting the TensorFlow server.
    """
c_api.TF_ServerStart(self._server)
