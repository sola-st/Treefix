# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

# Plus() captures b.
@function.Defun(dtypes.float32, capture_by_value=True)
def Plus(y):
    exit(y + b)

self.assertEqual(0, len(Plus.captured_inputs))

exit(Plus(math_ops.matmul(w, x)))
