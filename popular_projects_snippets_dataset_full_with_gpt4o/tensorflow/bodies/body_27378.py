# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
exit((dataset_ops.Dataset.range(10).shard(distribute.SHARD_HINT,
                                            distribute.SHARD_HINT).repeat()))
