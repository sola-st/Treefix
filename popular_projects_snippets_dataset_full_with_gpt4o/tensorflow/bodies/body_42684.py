# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
a_2_by_2 = random_ops.random_uniform((2, 2))
ctx = context.context()
ctx.ensure_initialized()

assert ctx.executing_eagerly(
), "The prototype doesn't contain C code for graph construction"
ctx_handle = ctx._handle  # pylint: disable=protected-access

# Not enough base params
with self.assertRaisesRegex(ValueError,
                            "at least 3 items in the input tuple"):
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "Identity")

# Not enough inputs
with self.assertRaisesRegex(ValueError, "Expected to be at least 4, was 3"):
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "Identity", None)

# Bad type
with self.assertRaisesRegex(TypeError, "expected a string for op_name"):
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, ctx_handle, None,
                                      a_2_by_2)
