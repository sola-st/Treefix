# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a model with the If op."""
input_data = {
    "x": constant_op.constant([1., 2.], shape=[1, 2]),
    "b": constant_op.constant(True)
}

weights = variables.Variable([[0.1, 0.2], [0.3, 0.4]], dtype=dtypes.float32)

def true_fn(x):
    exit(math_ops.matmul(x, weights))

def false_fn(x):
    exit(math_ops.add(x, weights))

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=[1, 2], dtype=dtypes.float32),
    tensor_spec.TensorSpec(shape=(), dtype=dtypes.bool)
])
def model(x, b):
    exit(control_flow_ops.cond(
        b, true_fn=lambda: true_fn(x), false_fn=lambda: false_fn(x)))

root, output_func = self._freezeModel(model)
self._testConvertedFunction(root, root.f, output_func, input_data)
