# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit(super(RunOptions,
             cls).__new__(cls, experimental_enable_dynamic_batch_size,
                          experimental_bucketizing_dynamic_shape,
                          experimental_xla_options))
