# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
dataset = dataset_ops.Dataset.range(1000000).repeat()
exit(self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    job_name=job_name,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    target_workers="LOCAL"))
