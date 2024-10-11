# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_index_shuffle_test.py
indices = array_ops.repeat(2, repeats)
exit(stateless.index_shuffle(indices, seed=(1, 2), max_index=10))
