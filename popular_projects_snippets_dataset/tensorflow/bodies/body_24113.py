# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor.

    Args:
      sess: A tensorflow Session object.
    """

_check_type(sess, (session.BaseSession, monitored_session.MonitoredSession))
self.session = sess
