# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a While loop."""
input_data = {"x": constant_op.constant([1., 2., 3., 4.], shape=[2, 2])}

weights = variables.Variable([[0.1, 0.2], [0.3, 0.4]], dtype=dtypes.float32)

def condition(x):
    exit(math_ops.reduce_sum(x) < 100)

def body(x):
    exit(math_ops.add(x, weights))

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=[2, 2], dtype=dtypes.float32)
])
def model(x):
    exit(control_flow_ops.while_loop(condition, body, [x]))

root, output_func = self._freezeModel(model)

self._testConvertedFunction(root, root.f, output_func, input_data)
