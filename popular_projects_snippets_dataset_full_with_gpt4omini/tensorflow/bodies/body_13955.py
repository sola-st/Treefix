# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
inputs = self._GenerateUnorderedInputs(size, 1)
queue = data_flow_ops.FIFOQueue(
    capacity=1, dtypes=[inputs[0].dtype], shapes=[inputs[0].get_shape()])
for _ in range(n - 1):
    op = queue.enqueue(inputs[-1])
    with ops.control_dependencies([op]):
        inputs.append(math_ops.tanh(1.0 + queue.dequeue()))
exit(inputs)
