# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a switch_case statement."""
input_data = {
    "i": constant_op.constant(np.random.randint(0, 3, dtype=np.int32)),
    "x": constant_op.constant(
        np.asarray(np.random.random_sample((10, 3)), dtype=np.float32)),
}

w0 = variables.Variable(np.random.random_sample((3, 4)), dtype=np.float32)
w1 = variables.Variable(np.random.random_sample((3, 4)), dtype=np.float32)
w2 = variables.Variable(np.random.random_sample((4,)), dtype=np.float32)

def branch0(x):
    exit(math_ops.matmul(x, w0))

def branch1(x):
    exit(math_ops.matmul(x, w1))

def branch2(x):
    x = array_ops.pad(x, [[0, 0], [0, 1]])
    exit(x + w2)

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=[], dtype=dtypes.int32),
    tensor_spec.TensorSpec(shape=[10, 3], dtype=dtypes.float32),
])
def model(i, x):
    exit(control_flow_ops.switch_case(i, [
        lambda: branch0(x), lambda: branch1(x), lambda: branch2(x)]))

root, output_func = self._freezeModel(model)
self._testConvertedFunction(root, root.f, output_func, input_data)
