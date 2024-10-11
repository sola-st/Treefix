# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Sets the global TensorFlow session.

  Args:
      session: A TF Session.
  """
global _SESSION
_SESSION.session = session
