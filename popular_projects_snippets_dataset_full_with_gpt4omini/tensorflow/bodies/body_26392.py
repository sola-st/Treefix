# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
dataset = dataset_ops.Dataset.range(10000)
for _ in range(chain_length):
    dataset = map_op._MapDataset(  # pylint: disable=protected-access
        dataset, fn, use_inter_op_parallelism=use_inter_op_parallelism)
self.run_and_report_benchmark(
    dataset,
    num_elements=10000,
    extras={
        "model_name": "map.benchmark.%d" % benchmark_id,
        "parameters": "%d" % chain_length,
    },
    name="chain_length_%d%s" % (chain_length, label))
