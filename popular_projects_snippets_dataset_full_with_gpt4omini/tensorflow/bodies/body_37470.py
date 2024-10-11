# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_image_op_test.py
np.random.seed(7)
for depth in (1, 3, 4):
    with self.session(graph=ops.Graph()) as sess:
        shape = (4, 5, 7) + (depth,)

        # Build a random uint8 image
        images = np.random.randint(256, size=shape).astype(np.uint8)
        tf_images = ops.convert_to_tensor(images)
        self.assertEqual(tf_images.dtype, dtypes.uint8)

        # Summarize
        summ = summary.image("img", tf_images)
        value = self.evaluate(summ)
        self.assertEqual([], summ.get_shape())
        image_summ = self._AsSummary(value)

        # Decode the first image and check consistency.
        # Since we're uint8, everything should be exact.
        image = image_ops.decode_png(image_summ.value[0]
                                     .image.encoded_image_string).eval()
        self.assertAllEqual(image, images[0])

        # Check the rest of the proto
        self._CheckProto(image_summ, shape)
