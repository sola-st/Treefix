# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/snapshot_dataset_benchmark.py
num_elements = 100000
tmp_dir = self._makeSnapshotDirectory()
dataset = self._createSimpleDataset(
    num_elements=num_elements, tmp_dir=tmp_dir)

# consume all the elements to let snapshot write things to disk
self.run_benchmark(
    dataset=dataset,
    num_elements=num_elements,
    iters=1,
    warmup=False,
    apply_default_optimizations=True)
# Now run the actual benchmarks and report them
self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=num_elements,
    name="read_simple",
    extras={
        "model_name": "snapshot.benchmark.5",
        "parameters": "%d" % num_elements,
    })
