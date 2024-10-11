# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
shape = constant_op.constant([5])
if include_print:
    shape = logging_ops.Print(shape, [shape])
exit(random.get_global_generator().normal(shape))
