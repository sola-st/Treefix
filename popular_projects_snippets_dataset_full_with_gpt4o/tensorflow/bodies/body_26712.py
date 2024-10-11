# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/snapshot_dataset_benchmark.py
num_elements = 500000
dataset = self._createSimpleDataset(
    num_elements=num_elements, compression=snapshot.COMPRESSION_SNAPPY)

self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=num_elements,
    name="write_snappy",
    warmup=False,
    extras={
        "model_name": "snapshot.benchmark.2",
        "parameters": "%d" % num_elements,
    },
    iters=1)
