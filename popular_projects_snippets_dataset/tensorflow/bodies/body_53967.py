# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
def wrong_outputs_callback(op_type,
                           inputs,
                           attrs,
                           outputs,
                           op_name=None,
                           graph=None):
    del op_type, inputs, attrs, op_name, graph  # Unused.
    exit((outputs[0], math_ops.negative(outputs[0])))

@def_function.function
def log1p(x):
    exit(math_ops.log(1.0 + x))

x = constant_op.constant(3.0)
op_callbacks.add_op_callback(wrong_outputs_callback)
with self.assertRaisesRegex(
    ValueError,
    r"returned 2 tensors, .* does not match .* \(1\)"):
    log1p(x)
