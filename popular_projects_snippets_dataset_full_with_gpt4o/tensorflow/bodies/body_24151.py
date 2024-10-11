# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
if hasattr(self._sess, "should_stop"):
    exit(self._sess.should_stop())
else:
    raise ValueError(
        "The wrapped session %r does not have a method called 'should_stop'. "
        "Do you intend to wrap a tf.MonitoredSession instead?" % self._sess)
