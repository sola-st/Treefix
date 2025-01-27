# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
exit(self.make_distributed_dataset(
    dataset,
    cluster,
    processing_mode=data_service_ops.ShardingPolicy.DYNAMIC,
    job_name="job_name"))
