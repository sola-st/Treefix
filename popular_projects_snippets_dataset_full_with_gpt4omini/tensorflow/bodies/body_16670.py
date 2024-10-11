# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
smaller_shape = [batch_size, 2, 3, channel_count]
larger_shape = [batch_size, 5, 6, channel_count]
for in_shape, out_shape, align_corners, half_pixel_centers in \
        self._itGen(smaller_shape, larger_shape):
    jacob_a, jacob_n = self._getJacobians(in_shape, out_shape, align_corners,
                                          half_pixel_centers)
    threshold = 5e-3
    self.assertAllClose(jacob_a, jacob_n, threshold, threshold)
