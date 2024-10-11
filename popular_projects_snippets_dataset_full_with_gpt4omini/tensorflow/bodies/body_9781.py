# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Closes this session.

    Calling this method frees all resources associated with the session.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        closing the TensorFlow session.
    """
if self._session and not self._closed:
    self._closed = True
    tf_session.TF_CloseSession(self._session)
