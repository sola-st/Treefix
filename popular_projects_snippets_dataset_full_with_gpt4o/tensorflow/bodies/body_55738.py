# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
if use_mlir:
    SetTracingImplementation("mlir")

def model(t):
    exit(unified_nn_ops.relu(t))

with context_lib.set_default(get_immediate_execution_context()):
    positive = TensorCastHelper(constant_op.constant([1.]))
    negative = TensorCastHelper(constant_op.constant([-1.]))

    model_fn = def_function.function(model)
    func_output = model_fn(positive)
    self.assertAllEqual(func_output.numpy(), [1.])
    func_output = model_fn(negative)
    self.assertAllEqual(func_output.numpy(), [0.])

    eager_output = model(positive)
    self.assertAllEqual(eager_output.numpy(), [1.])
    eager_output = model(negative)
    self.assertAllEqual(eager_output.numpy(), [0.])
