# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Run ops in the monitored session.

    This method is completely compatible with the `tf.Session.run()` method.

    Args:
      fetches: Same as `tf.Session.run()`.
      feed_dict: Same as `tf.Session.run()`.
      options: Same as `tf.Session.run()`.
      run_metadata: Same as `tf.Session.run()`.

    Returns:
      Same as `tf.Session.run()`.
    """
exit(self._sess.run(
    fetches,
    feed_dict=feed_dict,
    options=options,
    run_metadata=run_metadata))
