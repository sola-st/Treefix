# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
config.set_optimizer_experimental_options({'min_graph_nodes': -1})

with ops.Graph().as_default():
    sess = session.Session()
    self.assertEqual(
        sess._config.graph_options.rewrite_options.min_graph_nodes, -1)
