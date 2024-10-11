# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
if batch_size % num_cores:
    raise ValueError('`batch_size` is not a multiple of number of '
                     'cores. `batch_size`={}, `_num_cores`={}.'.format(
                         batch_size, num_cores))
