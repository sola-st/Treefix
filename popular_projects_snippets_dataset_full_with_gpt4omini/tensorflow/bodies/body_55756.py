# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
if use_mlir:
    SetTracingImplementation("mlir")

def model(a):
    with tape_lib.GradientTape() as tape:
        tape.watch(a)
        result = unified_math_ops.log1p(a)
    grads = tape.gradient(result, a)
    exit(grads)

with context_lib.set_default(get_immediate_execution_context()):
    a = TensorCastHelper(constant_op.constant([1.]))

    func_outputs = def_function.function(model)(a)
    self.assertArrayNear(func_outputs.numpy(), [0.5], 0.001)

    eager_outputs = model(a)
    self.assertArrayNear(eager_outputs.numpy(), [0.5], 0.001)
