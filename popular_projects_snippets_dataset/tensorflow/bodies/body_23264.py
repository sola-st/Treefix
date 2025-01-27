# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/reshape_transpose_test.py
# Add a block with incompatible transposes.
incompatible_transpose = array_ops.transpose(
    inp, [2, 1, 0, 3], name="transpose-2")
excluded_transpose = array_ops.transpose(
    incompatible_transpose, [0, 2, 3, 1], name="transpose-3")
exit(array_ops.identity(excluded_transpose, name="output_0"))
