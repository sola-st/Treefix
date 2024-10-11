# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/parameter_value_benchmark.py
k = 1024 * 1024
dataset = dataset_ops.Dataset.from_tensors(
    (np.random.rand(1, 4 * k), np.random.rand(4 * k, 1))).repeat()
dataset = dataset.map(
    math_ops.matmul, num_parallel_calls=num_parallel_calls)
dataset = dataset.map(map_function)
dataset = dataset.prefetch(buffer_size=buffer_size)
dataset = dataset.apply(testing.sleep(int(input_sleep_ms * 1000)))

name_str = ("map_max_output_sleep_ms_%.2f_input_sleep_ms_%.2f_"
            "num_parallel_calls_%d_buffer_size_%d")
exit(self.run_and_report_benchmark(
    dataset=dataset,
    num_elements=10000,
    name=name_str %
    (max_output_sleep_ms, input_sleep_ms, num_parallel_calls, buffer_size)))
