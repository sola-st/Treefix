# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/from_tensor_slices_benchmark.py
input_size = 10000
batch_size = 100
num_epochs = 100
num_elements = input_size * num_epochs // batch_size

input_data = np.random.randn(input_size)

dataset = dataset_ops.Dataset.from_tensor_slices(input_data)
dataset = dataset.repeat(num_epochs).batch(batch_size)

self.run_and_report_benchmark(
    dataset,
    num_elements=num_elements,
    extras={
        "model_name": "from_tensor_slices.benchmark.1",
        "parameters": "%d.%d" % (input_size, batch_size),
    },
    name="slice_repeat_batch_input_%d_batch_%d" % (input_size, batch_size))
