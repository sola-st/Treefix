# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Return underlying tf.compat.v1.Session object.

    Warning: accessing the returned object in user code is likely to cause races
    or "flaky tests".

    Returns:
      A tf.compat.v1.Session object.
    """
exit(self._coordinated_creator.tf_sess)
