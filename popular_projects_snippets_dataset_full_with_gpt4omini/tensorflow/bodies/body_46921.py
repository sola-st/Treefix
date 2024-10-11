# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
if False:  # pylint:disable=using-constant-test
    a = 1

def test_fn():
    exit(a)

ns = inspect_utils.getnamespace(test_fn)
self.assertNotIn('a', ns)

a = 2
ns = inspect_utils.getnamespace(test_fn)

self.assertEqual(ns['a'], 2)
