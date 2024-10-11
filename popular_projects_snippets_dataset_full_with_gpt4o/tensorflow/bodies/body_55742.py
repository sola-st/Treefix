# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
if use_mlir:
    SetTracingImplementation("mlir")

def model(a):
    exit(unified_math_ops.neg(a))

with context_lib.set_default(get_immediate_execution_context()):
    a = TensorCastHelper(constant_op.constant([2.]))

    func_output = def_function.function(model)(a)
    self.assertAllEqual(func_output.numpy(), [-2.])

    eager_output = model(a)
    self.assertAllEqual(eager_output.numpy(), [-2.])
