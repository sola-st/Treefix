# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
global_batch_size = 8
batch_size = input_context.get_per_replica_batch_size(global_batch_size)
dataset = dataset_ops.DatasetV2.range(14).batch(
    batch_size, drop_remainder=False)
exit(dataset.shard(input_context.num_input_pipelines,
                     input_context.input_pipeline_id))
