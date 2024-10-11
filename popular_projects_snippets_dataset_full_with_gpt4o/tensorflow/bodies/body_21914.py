# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    x = array_ops.placeholder(dtype=dtypes.int64)
    with self.assertRaisesRegex(ValueError, "Cannot infer Tensor's rank"):
        inp.batch_join([[x]], batch_size=2)
