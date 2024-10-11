# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
dataset_id = _register_dataset(service, dataset, compression=compression)
exit(_from_dataset_id(
    processing_mode,
    service,
    dataset_id,
    dataset.element_spec,
    job_name=job_name,
    consumer_index=consumer_index,
    num_consumers=num_consumers,
    max_outstanding_requests=max_outstanding_requests,
    task_refresh_interval_hint_ms=task_refresh_interval_hint_ms,
    data_transfer_protocol=data_transfer_protocol,
    compression=compression,
    cross_trainer_cache=cross_trainer_cache,
    target_workers=target_workers))
