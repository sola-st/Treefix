# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
with ops.Graph().as_default() as graph:
    num_constant = constant_op.constant(num)
    with self.session(graph=graph, force_gpu=self.force_gpu):
        tf_ans = math_ops.linspace_nd(start, stop, num_constant, axis=axis)
        exit(self.evaluate(tf_ans))
