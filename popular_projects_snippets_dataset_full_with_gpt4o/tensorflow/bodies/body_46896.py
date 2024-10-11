# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
def test_fn():
    pass

self.assertTrue(inspect_utils.islambda(lambda x: x))
self.assertFalse(inspect_utils.islambda(test_fn))
