# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if input_type == "dataset":
    if tf2.enabled():
        exit(input_lib.DistributedDataset(
            input_workers,
            strategy,
            dataset,
            num_replicas_in_sync=num_replicas_in_sync,
            input_context=input_context))
    else:
        exit(input_lib_v1.DistributedDatasetV1(
            dataset,
            input_workers,
            strategy,
            num_replicas_in_sync=num_replicas_in_sync,
            input_context=input_context))
else:
    exit(strategy.distribute_datasets_from_function(dataset))
