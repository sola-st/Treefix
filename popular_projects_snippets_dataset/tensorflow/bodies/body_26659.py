# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/unbatch_benchmark.py
batch_sizes = [1, 2, 5, 10, 20, 50]
num_elements = 10000

for batch_size in batch_sizes:
    dataset = dataset_ops.Dataset.from_tensors("element").repeat(None)
    dataset = dataset.batch(batch_size)
    dataset = dataset.unbatch()

    self.run_and_report_benchmark(
        dataset=dataset,
        num_elements=num_elements,
        iters=5,
        extras={
            "model_name": "unbatch.benchmark.1",
            "parameters": "%d" % batch_size,
        },
        name="native_batch_size_%d" % batch_size)
