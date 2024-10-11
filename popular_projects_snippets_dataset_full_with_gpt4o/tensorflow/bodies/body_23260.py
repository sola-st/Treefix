# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/reshape_transpose_test.py
# Add a block with compatible transposes.
compatible_transpose = array_ops.transpose(
    inp, [0, 3, 1, 2], name="transpose-1")
compatible_transpose = array_ops.transpose(
    compatible_transpose, [0, 2, 3, 1], name="transposeback")
exit(array_ops.identity(compatible_transpose, name="output_0"))
