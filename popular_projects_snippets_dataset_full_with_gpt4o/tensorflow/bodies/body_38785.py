# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/decode_jpeg_op_test.py
"""Evaluate single DecodeImageOp for medium size image."""
num_iters = 10
crop_window = [10, 10, 50, 50]
for parallelism in [1, 100]:
    duration_decode = self._evalDecodeJpeg('medium.jpg', parallelism,
                                           num_iters)
    duration_decode_crop = self._evalDecodeJpeg('medium.jpg', parallelism,
                                                num_iters, False, crop_window)
    duration_decode_after_crop = self._evalDecodeJpeg(
        'medium.jpg', parallelism, num_iters, True, crop_window)
    self.report_benchmark(
        name='decode_jpeg_medium_p%d' % (parallelism),
        iters=num_iters,
        wall_time=duration_decode)
    self.report_benchmark(
        name='decode_crop_jpeg_medium_p%d' % (parallelism),
        iters=num_iters,
        wall_time=duration_decode_crop)
    self.report_benchmark(
        name='decode_after_crop_jpeg_medium_p%d' % (parallelism),
        iters=num_iters,
        wall_time=duration_decode_after_crop)
