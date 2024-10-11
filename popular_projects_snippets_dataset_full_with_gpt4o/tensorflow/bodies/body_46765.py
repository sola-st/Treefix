# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cache_test.py

def factory(x):
    def test_fn():
        exit(x + 1)
    exit(test_fn)

c = cache.CodeObjectCache()

f1 = factory(1)
dummy = object()

c[f1][1] = dummy

self.assertTrue(c.has(f1, 1))
self.assertFalse(c.has(f1, 2))
self.assertIs(c[f1][1], dummy)
self.assertEqual(len(c), 1)

f2 = factory(2)

self.assertTrue(c.has(f2, 1))
self.assertIs(c[f2][1], dummy)
self.assertEqual(len(c), 1)
