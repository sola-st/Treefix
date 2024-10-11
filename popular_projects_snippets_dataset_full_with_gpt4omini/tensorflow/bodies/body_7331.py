# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
dataset = dataset_ops.DatasetV2.from_tensor_slices([fname1, fname2])
dataset = dataset.shard(input_context.num_input_pipelines,
                        input_context.input_pipeline_id)
exit(readers.TextLineDatasetV2(dataset).map(
    string_ops.string_to_number).batch(
        input_context.get_per_replica_batch_size(4)))
