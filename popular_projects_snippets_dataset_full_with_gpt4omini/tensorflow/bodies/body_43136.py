# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
original_global_dispatchers = dispatch._GLOBAL_DISPATCHERS
try:
    TensorTracerOpDispatcher().register()

    x = TensorTracer("x")
    y = TensorTracer("y")
    trace = math_ops.reduce_sum(math_ops.add(math_ops.abs(x), y), axis=3)
    self.assertEqual(
        str(trace), "math.reduce_sum(math.add(math.abs(x), y), axis=3)")

    proto_val = TensorTracer("proto")
    trace = decode_proto(proto_val, "message_type", ["field"], ["float32"])
    self.assertIn("io.decode_proto(bytes=proto,", str(trace))

finally:
    # Clean up.
    dispatch._GLOBAL_DISPATCHERS = original_global_dispatchers
