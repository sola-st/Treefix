# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
if use_mlir:
    SetTracingImplementation("mlir")

def model(a, b):
    with tape_lib.GradientTape() as tape:
        tape.watch(a)
        tape.watch(b)
        result = unified_math_ops.div_no_nan(a, b)
    grads = tape.gradient(result, [a, b])
    exit(grads)

with context_lib.set_default(get_immediate_execution_context()):
    a = TensorCastHelper(constant_op.constant([2.]))
    b = TensorCastHelper(constant_op.constant([4.]))

    func_outputs = def_function.function(model)(a, b)
    self.assertArrayNear(func_outputs[0].numpy(), [0.25], 0.001)
    self.assertArrayNear(func_outputs[1].numpy(), [-0.125], 0.001)

    eager_outputs = model(a, b)
    self.assertArrayNear(eager_outputs[0].numpy(), [0.25], 0.001)
    self.assertArrayNear(eager_outputs[1].numpy(), [-0.125], 0.001)
