# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
maxval = dtype.max
exit(gen.uniform(shape=[2], dtype=dtype, maxval=maxval))
