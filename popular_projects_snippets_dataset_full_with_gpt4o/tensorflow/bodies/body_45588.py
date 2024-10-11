# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

def h(l, a):
    exit(l(a) + 4000)

def g(a, *args):
    exit(a + sum(args))

def f(h, g, a, *args):
    exit(h(lambda x: g(x, *args), a))

tr, _ = self._transform_with_mock(f)

self.assertEqual(tr(h, g, 1, *(20, 300)), 4321)
