# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
for horizon in self._FORWARD_COMPATIBILITY_HORIZONS:
    with compat.forward_compatibility_horizon(*horizon):
        with self.cached_session():
            base = "tensorflow/core/lib/jpeg/testdata"
            jpeg0 = io_ops.read_file(os.path.join(base, "jpeg_merge_test1.jpg"))
            image0 = image_ops.decode_image(jpeg0, dtype=dtypes.uint16)
            image1 = image_ops.convert_image_dtype(image_ops.decode_jpeg(jpeg0),
                                                   dtypes.uint16)
            image0, image1 = self.evaluate([image0, image1])
            self.assertAllEqual(image0, image1)
