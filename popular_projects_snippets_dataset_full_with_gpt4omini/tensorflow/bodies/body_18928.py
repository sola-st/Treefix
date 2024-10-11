# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/compiled_collective_ops_gpu_test.py
context._reset_context()
gpus = config.list_physical_devices('GPU')
if len(gpus) < num_gpus:
    self.skipTest('Expected at least {} GPUs but found {} GPUs'.format(
        num_gpus, len(gpus)))
context.ensure_initialized()
