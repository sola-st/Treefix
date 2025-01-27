# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
# Supply dump root.
self._dump_root = dump_root

# Supply observer.
self._obs = observer

# Invoke superclass constructor.
framework.BaseDebugWrapperSession.__init__(
    self, sess, thread_name_filter=thread_name_filter)
