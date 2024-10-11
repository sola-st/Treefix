# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/snapshot_dataset_benchmark.py
num_elements = 500000
dataset = self._createSimpleDataset(num_elements=num_elements)

# We only run one iteration here because running multiple iterations will
# cause the later iterations to simply read from the already written
# snapshot rather than write a new one.
self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=num_elements,
    name="write_simple",
    warmup=False,
    extras={
        "model_name": "snapshot.benchmark.3",
        "parameters": "%d" % num_elements,
    },
    iters=1)
