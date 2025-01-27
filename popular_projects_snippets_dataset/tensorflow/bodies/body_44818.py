# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/testing.py
if self.raises_cm is not None:
    raise ValueError('cannot use more than one assertRaisesRuntime in a test')
self.raises_cm = self.assertRaisesRegex(*args)
self.raises_cm.__enter__()
