# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

class TestCallable:

    def __call__(self):
        pass

c = TestCallable()
self.assertEqual(inspect_utils.getmethodclass(c), TestCallable)
