# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
# skipTest() may be called in super().setUp()
if hasattr(self, '_backend_configurator'):
    self._backend_configurator.tearDown()
super().skipTest(reason)
