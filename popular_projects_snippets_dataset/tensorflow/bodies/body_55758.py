# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
if use_mlir:
    SetTracingImplementation("mlir")

def model(a, b):
    exit(unified_math_ops.div_no_nan(a, b))

with context_lib.set_default(get_immediate_execution_context()):
    a = TensorCastHelper(constant_op.constant([2.]))
    b = TensorCastHelper(constant_op.constant([4.]))

    func_output = def_function.function(model)(a, b)
    self.assertArrayNear(func_output.numpy(), [0.5], 0.001)

    eager_output = model(a, b)
    self.assertArrayNear(eager_output.numpy(), [0.5], 0.001)
