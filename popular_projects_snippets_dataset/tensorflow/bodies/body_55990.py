# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    for n_a in [0, 1, 3]:
        for n_b in [0, 1, 3]:
            for t_c in [[],
                        [dtypes.int32],
                        [dtypes.int32, dtypes.float32]]:
                a, b, c = op_def_library.apply_op(
                    "ComplexStruct", n_a=n_a, n_b=n_b, t_c=t_c)

                self.assertEqual(n_a, len(a))
                self.assertTrue(all(x.dtype == dtypes.int32 for x in a))
                self.assertEqual(n_b, len(b))
                self.assertTrue(all(x.dtype == dtypes.int64 for x in b))
                self.assertEqual(t_c, [x.dtype for x in c])
