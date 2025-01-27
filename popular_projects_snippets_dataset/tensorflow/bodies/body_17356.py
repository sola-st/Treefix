# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
for horizon in self._FORWARD_COMPATIBILITY_HORIZONS:
    with compat.forward_compatibility_horizon(*horizon):
        with self.cached_session():
            base = "tensorflow/core/lib/gif/testdata"
            gif0 = io_ops.read_file(os.path.join(base, "scan.gif"))

            # Test `expand_animations=False` case.
            image0 = image_ops.decode_image(
                gif0, dtype=dtypes.float32, expand_animations=False)
            # image_ops.decode_png() handles GIFs and returns 3D tensors
            animation = image_ops.decode_gif(gif0)
            first_frame = array_ops.gather(animation, 0)
            image1 = image_ops.convert_image_dtype(first_frame, dtypes.float32)
            image0, image1 = self.evaluate([image0, image1])
            self.assertLen(image0.shape, 3)
            self.assertAllEqual(list(image0.shape), [40, 20, 3])
            self.assertAllEqual(image0, image1)

            # Test `expand_animations=True` case.
            image2 = image_ops.decode_image(gif0, dtype=dtypes.float32)
            image3 = image_ops.convert_image_dtype(animation, dtypes.float32)
            image2, image3 = self.evaluate([image2, image3])
            self.assertLen(image2.shape, 4)
            self.assertAllEqual(list(image2.shape), [12, 40, 20, 3])
            self.assertAllEqual(image2, image3)
