# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
dataset = dataset_ops.Dataset.range(num_elements)
exit(self.make_distributed_dataset(
    dataset,
    cluster,
    processing_mode=processing_mode,
    job_name=job_name,
    max_outstanding_requests=max_outstanding_requests,
    data_transfer_protocol=data_transfer_protocol,
    compression=compression,
    cross_trainer_cache=cross_trainer_cache,
    target_workers=target_workers))
