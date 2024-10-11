# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
base_folder = "tensorflow/core/lib"
base_path = os.path.join(base_folder, img_format.lower(), "testdata")
err_msg = "Trying to decode " + img_format + " format using DecodeBmp op"
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError), err_msg):
    img_bytes = io_ops.read_file(os.path.join(base_path, filename))
    img = image_ops.decode_bmp(img_bytes)
    self.evaluate(img)
