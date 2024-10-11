# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/test.py
if pred():
    self.skipTest(skip_message)
else:
    exit(func(self, *args, **kwargs))
