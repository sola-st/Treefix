# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
for horizon in self._FORWARD_COMPATIBILITY_HORIZONS:
    with compat.forward_compatibility_horizon(*horizon):
        with test_util.use_gpu():
            base = "tensorflow/core/lib/bmp/testdata"
            # `rgba_transparent.bmp` has 4 channels with transparent pixels.
            # Test consistency between `decode_image` and `decode_bmp` functions.
            bmp0 = io_ops.read_file(os.path.join(base, "rgba_small.bmp"))
            image0 = image_ops.decode_image(bmp0, channels=4)
            image1 = image_ops.decode_bmp(bmp0, channels=4)
            image0, image1 = self.evaluate([image0, image1])
            self.assertAllEqual(image0, image1)

            # Test that 3 channels is returned with user request of `channels=3`
            # even though image has 4 channels.
            # Note that this operation simply drops 4th channel information. This
            # is the same behavior as `decode_png`.
            # e.g. pixel values [25, 25, 25, 100] becomes [25, 25, 25].
            bmp1 = io_ops.read_file(os.path.join(base, "rgb_small.bmp"))
            image2 = image_ops.decode_bmp(bmp0, channels=3)
            image3 = image_ops.decode_bmp(bmp1)
            image2, image3 = self.evaluate([image2, image3])
            self.assertAllEqual(image2, image3)

            # Test that 4 channels is returned with user request of `channels=4`
            # even though image has 3 channels. Alpha channel should be set to
            # UINT8_MAX.
            bmp3 = io_ops.read_file(os.path.join(base, "rgb_small_255.bmp"))
            bmp4 = io_ops.read_file(os.path.join(base, "rgba_small_255.bmp"))
            image4 = image_ops.decode_bmp(bmp3, channels=4)
            image5 = image_ops.decode_bmp(bmp4)
            image4, image5 = self.evaluate([image4, image5])
            self.assertAllEqual(image4, image5)

            # Test that 3 channels is returned with user request of `channels=3`
            # even though image has 1 channel (grayscale).
            bmp6 = io_ops.read_file(os.path.join(base, "grayscale_small.bmp"))
            bmp7 = io_ops.read_file(
                os.path.join(base, "grayscale_small_3channels.bmp"))
            image6 = image_ops.decode_bmp(bmp6, channels=3)
            image7 = image_ops.decode_bmp(bmp7)
            image6, image7 = self.evaluate([image6, image7])
            self.assertAllEqual(image6, image7)

            # Test that 4 channels is returned with user request of `channels=4`
            # even though image has 1 channel (grayscale). Alpha channel should be
            # set to UINT8_MAX.
            bmp9 = io_ops.read_file(
                os.path.join(base, "grayscale_small_4channels.bmp"))
            image8 = image_ops.decode_bmp(bmp6, channels=4)
            image9 = image_ops.decode_bmp(bmp9)
            image8, image9 = self.evaluate([image8, image9])
            self.assertAllEqual(image8, image9)
