# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
original_global_dispatchers = dispatch._GLOBAL_DISPATCHERS
try:
    TensorTracerOpDispatcher().register()

    x = TensorTracer("x")
    y = TensorTracer("y")
    trace = math_ops.add(
        math_ops.abs(ops.convert_to_tensor_v2_with_dispatch(x)), y)
    self.assertEqual(
        str(trace), "math.add(math.abs(convert_to_tensor(x)), y)")

finally:
    # Clean up.
    dispatch._GLOBAL_DISPATCHERS = original_global_dispatchers
