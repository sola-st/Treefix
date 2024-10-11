# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/snapshot_dataset_benchmark.py
num_elements = 100000
tmp_dir = self._makeSnapshotDirectory()
dataset = self._createSimpleDataset(
    num_elements=num_elements, tmp_dir=tmp_dir)

# Consume only 1 element, thus making sure we don't finalize.
self.run_benchmark(
    dataset=dataset,
    num_elements=1,
    iters=1,
    warmup=False,
    apply_default_optimizations=True)
# Now run the actual benchmarks and report them
self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=num_elements,
    name="passthrough_simple",
    extras={
        "model_name": "snapshot.benchmark.4",
        "parameters": "%d" % num_elements,
    },
)
