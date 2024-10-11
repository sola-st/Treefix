# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
# Destroy workers before the dispatcher for clean shutdown.
self.workers.clear()
del self.dispatcher
