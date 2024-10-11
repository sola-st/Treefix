# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
ctx = context.context()
ctx.ensure_initialized()

try:
    math_ops.mat_mul([[1., 1.] * 2], [[1., 1.] * 3])
except errors.InvalidArgumentError:
    etype, value, tb = sys.exc_info()
    full_exception_text = " ".join(
        traceback.format_exception(etype, value, tb))

self.assertNotRegex(full_exception_text, "_FallbackException")
