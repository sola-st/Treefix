# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
# pylint: disable=protected-access
exit(dataset.apply(
    data_service_ops._distribute(
        processing_mode,
        cluster.dispatcher_address(),
        job_name=job_name,
        consumer_index=consumer_index,
        num_consumers=num_consumers,
        max_outstanding_requests=max_outstanding_requests,
        task_refresh_interval_hint_ms=20,
        data_transfer_protocol=data_transfer_protocol,
        compression=compression,
        cross_trainer_cache=cross_trainer_cache,
        target_workers=target_workers)))
