# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
exit(xla.reduce(
    x, init_value=0, dimensions_to_reduce=dims, reducer=sum_reducer))
