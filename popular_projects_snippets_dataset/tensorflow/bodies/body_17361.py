# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
base = "tensorflow/core/lib/bmp/testdata"
bmp0 = io_ops.read_file(os.path.join(base, "rgba_small.bmp"))
err_msg = ("Trying to decode BMP format using a wrong op. Use `decode_bmp` "
           "or `decode_image` instead. Op used: ") + op_used
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError), err_msg):
    img = decode_op(bmp0)
    self.evaluate(img)
