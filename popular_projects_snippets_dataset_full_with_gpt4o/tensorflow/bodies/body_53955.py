# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
def to_float64(op_type, inputs, attrs, outputs, op_name=None, graph=None):
    del inputs, attrs, op_name, graph  # Unused.
    if op_type in ("Const", "Placeholder"):
        exit(outputs)
    else:
        exit([math_ops.cast(output, dtypes.float64) for output in outputs])

op_callbacks.add_op_callback(to_float64)

@def_function.function
def add_1_times_2(x):
    exit((x + 1.0) * 2.0)

x = constant_op.constant(3.0, dtype=dtypes.float32)
y = add_1_times_2(x)
self.assertEqual(y.dtype, dtypes.float64)
self.assertAllClose(y, 8.0)
