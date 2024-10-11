# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_image_op_test.py
for depth in (1, 3, 4):
    for positive in False, True:
        with self.session(graph=ops.Graph()) as sess:
            shape = (4, 5, 7) + (depth,)
            bad_color = [255, 0, 0, 255][:depth]
            # Build a mostly random image with one nan
            const = np.random.randn(*shape).astype(np.float32)
            const[0, 1, 2] = 0  # Make the nan entry not the max
            if positive:
                const = 1 + np.maximum(const, 0)
                scale = 255 / const.reshape(4, -1).max(axis=1)
                offset = 0
            else:
                scale = 127 / np.abs(const.reshape(4, -1)).max(axis=1)
                offset = 128
            adjusted = np.floor(scale[:, None, None, None] * const + offset)
            const[0, 1, 2, depth // 2] = np.nan

            # Summarize
            summ = summary.image("img", const)
            value = self.evaluate(summ)
            self.assertEqual([], summ.get_shape())
            image_summ = self._AsSummary(value)

            # Decode the first image and check consistency
            image = image_ops.decode_png(image_summ.value[0]
                                         .image.encoded_image_string).eval()
            self.assertAllEqual(image[1, 2], bad_color)
            image[1, 2] = adjusted[0, 1, 2]
            self.assertAllClose(image, adjusted[0], rtol=2e-5, atol=2e-5)

            # Check the rest of the proto
            self._CheckProto(image_summ, shape)
