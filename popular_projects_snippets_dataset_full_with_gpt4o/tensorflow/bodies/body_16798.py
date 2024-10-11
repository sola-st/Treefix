# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    self._testCollectiveReduce(inputs=[0.1, 0.3], expected=0.2,
                               set_graph_key=True)
