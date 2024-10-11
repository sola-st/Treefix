# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
smaller_shape = [batch_size, 4, 6, channel_count]
larger_shape = [batch_size, 8, 16, channel_count]
for params in self._itGen(smaller_shape, larger_shape):
    self._gpuVsCpuCase(*params, dtype=np.float32)
