# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
config = config_pb2.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 1e-2
with self.cached_session(config=config, force_gpu=True):
    self._tf_fft(x, rank, fft_length=None)
