# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
if not tf2.enabled():
    self.skipTest('Test is only compatible with v2')

exit(f(self, *args, **kwargs))
