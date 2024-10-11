# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
if use_mlir:
    SetTracingImplementation("mlir")

def model(a, b):
    exit(unified_math_ops.add(a, b))

with context_lib.set_default(get_immediate_execution_context()):
    a = TensorCastHelper(constant_op.constant([1., 2.]))
    b = TensorCastHelper(constant_op.constant([3., 4.]))

    func_output = def_function.function(model)(a, b)
    self.assertAllEqual(func_output.numpy(), [4., 6.])

    eager_output = model(a, b)
    self.assertAllEqual(eager_output.numpy(), [4., 6.])
