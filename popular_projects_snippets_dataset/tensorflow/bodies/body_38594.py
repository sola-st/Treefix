# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# If no GPU available, skip the test
if not test.is_gpu_available(cuda_only=True):
    exit()

# Draw 10 random shapes with large dimension sizes.
# 40% prob to generate dim[0] size within [1, 2047]
# 40% prob to generate dim[0] size within [2048, 4095]
# 20% prob to generate dim[0] size within [4096, 100000]
# 50% prob to use dim[1] as the small dim (<16)
num_samples = 10
total_size = 500000
small_size_limit = 2048
large_size_limit = 95905
small_size_percentage = 0.4
medium_size_percentage = 0.4
large_size_percentage = 0.2
perms = [[0, 2, 1]] * num_samples
dim_zero_sizes = []
dim_zero_sizes += list(
    np.random.randint(
        small_size_limit, size=int(small_size_percentage * num_samples)) +
    1)
dim_zero_sizes += list(
    np.random.randint(
        small_size_limit, size=int(medium_size_percentage * num_samples)) +
    small_size_limit)
dim_zero_sizes += list(
    np.random.randint(
        large_size_limit, size=int(large_size_percentage * num_samples)) +
    small_size_limit * 2)
input_shapes = []
small_dim_limit = 16
for dim_zero_size in dim_zero_sizes:
    small_dim_size = np.random.randint(small_dim_limit - 1) + 1
    large_dim_size = int(
        total_size / dim_zero_size / small_dim_size) + small_dim_limit
    input_shapes += ([[dim_zero_size, small_dim_size, large_dim_size]]
                     if np.random.randint(2) else
                     [[dim_zero_size, large_dim_size, small_dim_size]])

for input_shape, perm in zip(input_shapes, perms):
    # generate input data with random ints from 0 to 9.
    with self.subTest(input_shape=input_shape, perm=perm):
        inp = np.random.randint(10, size=input_shape)
        np_ans = self._np_transpose(inp, perm)
        with self.cached_session():
            inx = ops.convert_to_tensor(inp)
            y = array_ops.transpose(inx, perm)
            tf_ans = self.evaluate(y)
        self.assertAllEqual(np_ans, tf_ans)
        self.assertShapeEqual(np_ans, y)
        self._ClearCachedSession()
