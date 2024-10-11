# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py

def benchmark_helper(chain_length, fn, use_inter_op_parallelism, label,
                     benchmark_id):
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

chain_lengths = [0, 1, 2, 5, 10, 20, 50]
for chain_length in chain_lengths:
    benchmark_helper(
        chain_length=chain_length,
        fn=lambda x: x + 1,
        use_inter_op_parallelism=True,
        label="",
        benchmark_id=1)
    benchmark_helper(
        chain_length=chain_length,
        fn=lambda x: x + 1,
        use_inter_op_parallelism=False,
        label="_single_threaded",
        benchmark_id=2)
    benchmark_helper(
        chain_length=chain_length,
        fn=lambda x: x,
        use_inter_op_parallelism=True,
        label="_short_circuit",
        benchmark_id=3)
