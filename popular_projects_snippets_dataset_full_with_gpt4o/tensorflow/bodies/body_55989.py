# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    for n_a in [0, 1, 3]:
        a, b = op_def_library.apply_op("MixedStruct", n_a=n_a)
        self.assertIsInstance(a, list)
        self.assertEqual(n_a, len(a))
        self.assertTrue(all(x.dtype == dtypes.int32 for x in a))
        self.assertIsInstance(b, ops.Tensor)
        self.assertEqual(dtypes.float32, b.dtype)
