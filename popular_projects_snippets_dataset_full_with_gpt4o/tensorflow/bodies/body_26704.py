# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/parameter_value_benchmark.py
nums_parallel_calls = [4, 8, 10]
buffer_sizes = [10, 50, 100, 150, 200, 250, 300]

parameters_list = []
wall_time_map = {}

for num_parallel_calls in nums_parallel_calls:
    for buffer_size in buffer_sizes:
        parameters = (num_parallel_calls, buffer_size)
        parameters_list.append(parameters)
        wall_time = self._benchmark_interleave(num_parallel_calls, buffer_size)
        wall_time_map[parameters] = wall_time

parameters_list.sort(key=lambda x: wall_time_map[x])
for parameters in parameters_list:
    print("num_parallel_calls_%d_buffer_size_%d_wall_time:" % parameters,
          wall_time_map[parameters])
