# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
input_data = [[[64, 32], [32, 64], [50, 100]], [[32, 16], [16, 32],
                                                [25, 50]]]
expected_data = [[[64.0, 64.0, 32.0, 32.0], [64.0, 64.0, 32.0, 32.0],
                  [32.0, 32.0, 64.0, 64.0], [32.0, 32.0, 64.0, 64.0],
                  [50.0, 50.0, 100.0, 100.0], [50.0, 50.0, 100.0, 100.0]],
                 [[32.0, 32.0, 16.0, 16.0], [32.0, 32.0, 16.0, 16.0],
                  [16.0, 16.0, 32.0, 32.0], [16.0, 16.0, 32.0, 32.0],
                  [25.0, 25.0, 50.0, 50.0], [25.0, 25.0, 50.0, 50.0]]]

for dtype in self.float_types:
    input_image = np.array(input_data, dtype=dtype)
    expected = np.array(expected_data, dtype=dtype)
    with self.session() as sess, self.test_scope():
        image = array_ops.placeholder(input_image.dtype)
        resized = gen_image_ops.resize_nearest_neighbor(
            image, [6, 4], align_corners=False, half_pixel_centers=True)
        out = sess.run(resized, {image: input_image[:, :, :, np.newaxis]})
        self.assertAllClose(expected[:, :, :, np.newaxis], out)
