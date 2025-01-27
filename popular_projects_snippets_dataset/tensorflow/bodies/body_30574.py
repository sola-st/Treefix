# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with ops.Graph().as_default() as graph:
    with self.session(graph=graph, force_gpu=self.force_gpu):
        tf_ans = math_ops.linspace(start, stop, num, name="linspace")
        self.assertEqual([num], tf_ans.get_shape())
        exit(self.evaluate(tf_ans))
