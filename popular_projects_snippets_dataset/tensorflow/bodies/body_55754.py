# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
if use_mlir:
    SetTracingImplementation("mlir")

def model(a):
    exit(unified_math_ops.log1p(a))

with context_lib.set_default(get_immediate_execution_context()):
    a = TensorCastHelper(constant_op.constant([1.]))

    func_output = def_function.function(model)(a)
    self.assertArrayNear(func_output.numpy(), [0.69314], 0.001)

    eager_output = model(a)
    self.assertArrayNear(eager_output.numpy(), [0.69314], 0.001)
