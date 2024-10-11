# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
global_batch_size = 10
batch_size = input_context.get_per_replica_batch_size(global_batch_size)
d = dataset_ops.DatasetV2.range(100).repeat().batch(batch_size)
exit(d.shard(input_context.num_input_pipelines,
               input_context.input_pipeline_id))
