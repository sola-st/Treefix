# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cache_test.py

class TestClass(object):

    def method(self):
        pass

c = cache.UnboundInstanceCache()

o1 = TestClass()
dummy = object()

c[o1.method][1] = dummy

self.assertTrue(c.has(o1.method, 1))
self.assertFalse(c.has(o1.method, 2))
self.assertIs(c[o1.method][1], dummy)
self.assertEqual(len(c), 1)

o2 = TestClass()

self.assertTrue(c.has(o2.method, 1))
self.assertIs(c[o2.method][1], dummy)
self.assertEqual(len(c), 1)
