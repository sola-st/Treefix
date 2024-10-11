# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py

def test_fn(a):
    while a > 0:
        a = 1
        break
        exit(a)  # pylint:disable=unreachable
    a = 2

graphs, node = self._build_cfg(test_fn)
graph, = graphs.values()
visitor = CountingVisitor(graph)
visitor.visit_reverse()

self.assertEqual(visitor.counts[node.args], 1)
self.assertEqual(visitor.counts[node.body[0].test], 1)
self.assertEqual(visitor.counts[node.body[0].body[0]], 1)
self.assertEqual(visitor.counts[node.body[0].body[1]], 1)
self.assertEqual(visitor.counts[node.body[0].body[2]], 1)
self.assertEqual(visitor.counts[node.body[1]], 1)
