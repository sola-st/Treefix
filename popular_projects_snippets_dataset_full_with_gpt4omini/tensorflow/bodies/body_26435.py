# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py

self._wrapped = _DataServiceDatasetV2(
    dataset_id=dataset_id,
    processing_mode=processing_mode,
    address=address,
    element_spec=element_spec,
    protocol=protocol,
    data_transfer_protocol=data_transfer_protocol,
    job_name=job_name,
    consumer_index=consumer_index,
    num_consumers=num_consumers,
    max_outstanding_requests=max_outstanding_requests,
    task_refresh_interval_hint_ms=task_refresh_interval_hint_ms,
    cross_trainer_cache=cross_trainer_cache,
    target_workers=target_workers)
super(_DataServiceDatasetV1, self).__init__(self._wrapped)
