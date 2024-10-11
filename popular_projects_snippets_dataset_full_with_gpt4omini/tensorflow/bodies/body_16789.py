# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    self._testCollectiveReduce(
        inputs=[[0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1],
                [0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3]],
        expected=[0.2, 1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2],
        set_graph_key=True,
        fp16=True)
