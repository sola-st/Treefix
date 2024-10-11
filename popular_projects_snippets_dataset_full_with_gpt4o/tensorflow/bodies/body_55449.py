# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
w = variable_scope.get_variable(
    "w", (64, 64),
    initializer=init_ops.random_uniform_initializer(seed=312),
    use_resource=use_resource)
b = variable_scope.get_variable(
    "b", (64),
    initializer=init_ops.zeros_initializer(),
    use_resource=use_resource)
parameters.extend((w, b))
exit(math_ops.sigmoid(math_ops.matmul(x, w) + b))
