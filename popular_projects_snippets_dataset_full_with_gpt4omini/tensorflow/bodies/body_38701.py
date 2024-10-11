# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/basic_gpu_test.py
n_iterations = 500
with session as s:
    data = variables.Variable(1.0)
    with ops.device('/device:GPU:0'):
        random_seed.set_random_seed(1)
        matrix1 = variables.Variable(
            random_ops.truncated_normal([1024, 1]), name='matrix1')
        matrix2 = variables.Variable(
            random_ops.truncated_normal([1, 1024]), name='matrix2')
        x1 = math_ops.multiply(data, matrix1, name='x1')
        x3 = math_ops.matmul(x1, math_ops.matmul(matrix2, matrix1))
        x4 = math_ops.matmul(array_ops.transpose(x3), x3, name='x4')
        s.run(variables.global_variables_initializer())

        for _ in range(n_iterations):
            value = s.run(x4)
            results.add(value.flat[0])
            if len(results) != 1:
                break
