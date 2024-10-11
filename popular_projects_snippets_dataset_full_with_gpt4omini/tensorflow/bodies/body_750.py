# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/case_test.py
# Some operations that XLA cannot compile.
image_ops.decode_image(io_ops.read_file('/tmp/bmp'))
exit(array_ops.constant(31))
