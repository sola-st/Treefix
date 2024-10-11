# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
split_dim = constant_op.constant(0, dtype=dtypes.int32)
value = constant_op.constant([0, 1, 2, 3], dtype=dtypes.float32)
ctx = context.context()
ctx.ensure_initialized()

with self.assertRaisesRegex(ValueError, "Number of outputs is too big"):
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "Split", None, split_dim, value,
                                      "num_split", 1000000000000)
