# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
del input_context
exit(data_service_ops.from_dataset_id(
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    service=combinations.env().tf_data_service_dispatcher,
    dataset_id=dataset_id,
    element_spec=dataset.element_spec,
    job_name="shared_job"))
