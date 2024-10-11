# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
original_global_dispatchers = dispatch._GLOBAL_DISPATCHERS
try:
    TensorTracerOpDispatcher().register()

    x = TensorTracer("x")
    trace = x[0]
    self.assertEqual(str(trace), "__operators__.getitem(x, 0)")

    x = TensorTracer("x")
    y = TensorTracer("y")
    trace = x[y]
    self.assertEqual(str(trace), "__operators__.getitem(x, y)")

    x = TensorTracer("x")
    y = TensorTracer("y")
    trace = x[:y]  # pylint: disable=invalid-slice-index
    self.assertEqual(
        str(trace), "__operators__.getitem(x, slice(None, y, None))")

    x = array_ops.ones(shape=(3, 3))
    y = TensorTracer("y")
    trace = x[y]
    self.assertEqual(str(trace), "__operators__.getitem(%s, y)" % x)

    trace = x[:y]  # pylint: disable=invalid-slice-index
    self.assertEqual(
        str(trace), "__operators__.getitem(%s, slice(None, y, None))" % x)

finally:
    # Clean up.
    dispatch._GLOBAL_DISPATCHERS = original_global_dispatchers
