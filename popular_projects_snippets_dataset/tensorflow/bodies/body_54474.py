# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default() as g:
    test_util.set_producer_version(g, 7)
    old = test_ops.old()
    with self.session(graph=g):
        old.run()
