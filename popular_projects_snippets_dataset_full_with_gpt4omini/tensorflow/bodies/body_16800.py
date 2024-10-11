# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    self._testCollectiveReduce(
        inputs=[[1., 20., 3., 40., 5.], [10., 2., 30., 4., 50.]],
        expected=[1., 2., 3., 4., 5.],
        set_graph_key=True,
        instance_key=40,
        merge_op='Min',
        final_op='Id')
