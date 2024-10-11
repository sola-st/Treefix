# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
size = input_tensor.shape.dims[1]
with variable_scope.variable_scope("linear", reuse=reuse):
    w = variable_scope.get_variable(
        "w", shape=[size, size], dtype=input_tensor.dtype)
exit(math_ops.matmul(input_tensor, w))
