# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/from_tensor_slices_benchmark.py
input_size = 10000
reshape_dim = [100, 100]
num_epochs = 100

num_elements = num_epochs * reshape_dim[0]

data = np.random.randn(input_size).reshape(*reshape_dim)
dataset = dataset_ops.Dataset.from_tensor_slices(data).repeat(num_epochs)

self.run_and_report_benchmark(
    dataset,
    num_elements=num_elements,
    extras={
        "model_name": "from_tensor_slices.benchmark.2",
        "parameters": "%d" % input_size,
    },
    name="reshape_slice_repeat_input_%d" % input_size,
)
