# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
"""Test that the graphdef version is plumbed through to kernels."""
with ops.Graph().as_default() as g:
    version = g.graph_def_versions.producer
    with self.session(graph=g):
        v = test_ops.graph_def_version().eval()
        self.assertEqual(version, v)
