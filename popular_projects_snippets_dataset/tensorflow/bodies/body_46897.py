# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
l = lambda x: 1
l.__name__ = 'f'
self.assertTrue(inspect_utils.islambda(l))
