# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/transpose_benchmark.py
print("transpose benchmark:")

datatypes = [np.complex128, np.float64, np.float32, np.float16, np.int8]

small_shapes = [[2, 20, 20, 20, 16], [2, 16, 20, 20, 20]] * 2
small_shapes += [[2, 100, 100, 16], [2, 16, 100, 100]] * 2
small_shapes += [[2, 5000, 16], [2, 16, 5000]] * 2
small_perms = [[0, 4, 1, 2, 3], [0, 2, 3, 4, 1]] + [[4, 1, 2, 3, 0]] * 2
small_perms += [[0, 3, 1, 2], [0, 2, 3, 1]] + [[3, 1, 2, 0]] * 2
small_perms += [[0, 2, 1]] * 2 + [[2, 1, 0]] * 2

large_shapes = [[2, 40, 40, 40, 32], [2, 40, 40, 40, 64]] * 2 + [[
    2, 300, 300, 32
], [2, 300, 300, 64]] * 2 + [[2, 100000, 32], [2, 100000, 64]] * 2
large_perms = [[0, 4, 1, 2, 3], [0, 2, 3, 4, 1]] + [[4, 1, 2, 3, 0]] * 2 + [
    [0, 3, 1, 2], [0, 2, 3, 1]
] + [[3, 1, 2, 0]] * 2 + [[0, 2, 1]] * 2 + [[2, 1, 0]] * 2

num_iters = 40
for datatype in datatypes:
    for ishape, perm in zip(small_shapes, small_perms):
        self._run_graph("gpu", ishape, perm, num_iters, datatype)

    if datatype is not np.complex128:
        if datatype is not np.float16:
            for ishape, perm in zip(large_shapes, large_perms):
                self._run_graph("gpu", ishape, perm, num_iters, datatype)

small_dim_large_shapes = [[2, 10000, 3], [2, 3, 10000], [2, 10000, 8],
                          [2, 8, 10000]]
small_dim_small_shapes = [[2, 5000, 3], [2, 3, 5000], [2, 5000, 8],
                          [2, 8, 5000]]
small_dim_perms = [[0, 2, 1]] * 4

num_iters = 320
small_dim_large_shape_datatypes = [np.float64, np.float32, np.int8]
for datatype in small_dim_large_shape_datatypes:
    for ishape, perm in zip(small_dim_large_shapes, small_dim_perms):
        self._run_graph("gpu", ishape, perm, num_iters, datatype)

small_dim_small_shape_datatypes = [np.complex128, np.float16]
for datatype in small_dim_small_shape_datatypes:
    for ishape, perm in zip(small_dim_small_shapes, small_dim_perms):
        self._run_graph("gpu", ishape, perm, num_iters, datatype)
