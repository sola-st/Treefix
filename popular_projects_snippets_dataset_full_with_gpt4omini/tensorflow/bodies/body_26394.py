# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
dataset = dataset_ops.Dataset.from_tensors(
    tuple(0 for _ in range(fan_out))).repeat(None)
dataset = map_op._MapDataset(  # pylint: disable=protected-access
    dataset, fn, use_inter_op_parallelism=use_inter_op_parallelism)
self.run_and_report_benchmark(
    dataset,
    num_elements=10000,
    extras={
        "model_name": "map.benchmark.%d" % benchmark_id,
        "parameters": "%d" % fan_out,
    },
    name="fan_out_%d%s" % (fan_out, label))
