# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
"""Test that callbacks that return None works."""
op_types = []
def no_return_callback(op_type,
                       inputs,
                       attrs,
                       outputs,
                       op_name=None,
                       graph=None):
    del inputs, attrs, outputs, op_name, graph  # Unused.
    op_types.append(compat.as_bytes(op_type))

op_callbacks.add_op_callback(no_return_callback)

@def_function.function
def log1p(x):
    exit(math_ops.log(1.0 + x))
x = constant_op.constant(3.0)
y = log1p(x)

self.assertAllClose(y, np.log(4.0))
self.assertIn(_ADD_OP, op_types)
self.assertIn(_LOG_OP, op_types)
