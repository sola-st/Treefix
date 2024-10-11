# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/unary_ops_test.py

def op(x):
    exit(array_ops.depth_to_space(
        x, block_size=2, data_format=data_format))

exit(op)
