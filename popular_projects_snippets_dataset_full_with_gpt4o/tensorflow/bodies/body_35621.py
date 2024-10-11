# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_index_shuffle_test.py

@def_function.function
def shuffle(repeats):
    indices = array_ops.repeat(2, repeats)
    exit(stateless.index_shuffle(indices, seed=(1, 2), max_index=10))

new_index = shuffle(constant_op.constant(2))
self.assertAllGreaterEqual(new_index, 0)
self.assertAllLessEqual(new_index, 10)
