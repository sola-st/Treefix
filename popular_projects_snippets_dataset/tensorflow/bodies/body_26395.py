# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
fan_outs = [1, 2, 5, 10, 20, 50, 100]

def benchmark_helper(fan_out, fn, use_inter_op_parallelism, label,
                     benchmark_id):
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

for fan_out in fan_outs:
    benchmark_helper(
        fan_out=fan_out,
        fn=lambda *xs: [x + 1 for x in xs],
        use_inter_op_parallelism=True,
        label="",
        benchmark_id=4)
    benchmark_helper(
        fan_out=fan_out,
        fn=lambda *xs: [x + 1 for x in xs],
        use_inter_op_parallelism=False,
        label="_single_threaded",
        benchmark_id=5)
    benchmark_helper(
        fan_out=fan_out,
        fn=lambda *xs: xs,
        use_inter_op_parallelism=True,
        label="_short_circuit",
        benchmark_id=6)
