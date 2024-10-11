# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
for horizon in self._FORWARD_COMPATIBILITY_HORIZONS:
    with compat.forward_compatibility_horizon(*horizon):
        with self.cached_session():
            base = "tensorflow/core/lib/gif/testdata"
            gif0 = io_ops.read_file(os.path.join(base, "scan.gif"))
            image0 = image_ops.decode_image(gif0, dtype=dtypes.float32)
            image1 = image_ops.convert_image_dtype(image_ops.decode_gif(gif0),
                                                   dtypes.float32)
            image0, image1 = self.evaluate([image0, image1])
            self.assertAllEqual(image0, image1)
