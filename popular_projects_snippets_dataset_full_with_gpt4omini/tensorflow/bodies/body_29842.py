# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
with ops.Graph().as_default() as g:
    large_array = np.zeros((256, 1024, 1024), dtype=np.float32)
    c = constant_op.constant(large_array)
    d = constant_op.constant(large_array)
    with self.assertRaisesRegex(ValueError,
                                "GraphDef cannot be larger than 2GB."):
        g.as_graph_def()
