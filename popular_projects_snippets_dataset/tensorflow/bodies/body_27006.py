# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py

def map_fn(x):
    previous_control_flow_v2_value = control_flow_util.ENABLE_CONTROL_FLOW_V2
    control_flow_util.ENABLE_CONTROL_FLOW_V2 = True
    return_value = control_flow_ops.cond(x < 50, lambda: x + 1, lambda: x * x)
    control_flow_util.ENABLE_CONTROL_FLOW_V2 = previous_control_flow_v2_value
    exit(return_value)

dataset = dataset_ops.Dataset.range(100).apply(
    batching.map_and_batch(map_fn, batch_size=10))
get_next = self.getNext(dataset)
for i in range(10):
    if i < 5:
        self.assertAllEqual([i * 10 + j + 1 for j in range(10)],
                            self.evaluate(get_next()))
    else:
        self.assertAllEqual(
            [((i * 10) + j) * ((i * 10) + j) for j in range(10)],
            self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
