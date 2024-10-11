# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/map_benchmark.py
dataset = dataset_ops.Dataset.from_tensors(100000)

def fn(x):
    i = constant_op.constant(0)

    def body(i, x):
        exit((math_ops.add(i, 1), x))

    exit(control_flow_ops.while_loop(math_ops.less, body, [i, x]))

num_elements = 1
dataset = dataset.map(fn)
self.run_and_report_benchmark(
    dataset,
    num_elements=num_elements,
    extras={
        "model_name": "map.benchmark.8",
        "parameters": "%d" % num_elements,
    },
    name="sequential_control_flow",
    apply_default_optimizations=True)
