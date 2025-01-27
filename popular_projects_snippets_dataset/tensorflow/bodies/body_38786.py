# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_jpeg_op_test.py
"""Evaluate single DecodeImageOp for large size image."""
num_iters = 10
crop_window = [10, 10, 50, 50]
tile = [4, 4, 1]
for parallelism in [1, 100]:
    # Tile the medium size image to composite a larger fake image.
    duration_decode = self._evalDecodeJpeg('medium.jpg', parallelism,
                                           num_iters, tile)
    duration_decode_crop = self._evalDecodeJpeg(
        'medium.jpg', parallelism, num_iters, False, crop_window, tile)
    duration_decode_after_crop = self._evalDecodeJpeg(
        'medium.jpg', parallelism, num_iters, True, crop_window, tile)
    self.report_benchmark(
        name='decode_jpeg_large_p%d' % (parallelism),
        iters=num_iters,
        wall_time=duration_decode)
    self.report_benchmark(
        name='decode_crop_jpeg_large_p%d' % (parallelism),
        iters=num_iters,
        wall_time=duration_decode_crop)
    self.report_benchmark(
        name='decode_after_crop_jpeg_large_p%d' % (parallelism),
        iters=num_iters,
        wall_time=duration_decode_after_crop)
