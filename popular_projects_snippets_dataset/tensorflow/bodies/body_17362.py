# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
base_folder = "tensorflow/core/lib"
base_path = os.path.join(base_folder, img_format.lower(), "testdata")
err_msg = ("DecodeAndCropJpeg operation can run on JPEG only, but "
           "detected ") + img_format
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError), err_msg):
    img_bytes = io_ops.read_file(os.path.join(base_path, filename))
    img = image_ops.decode_and_crop_jpeg(img_bytes, [1, 1, 2, 2])
    self.evaluate(img)
