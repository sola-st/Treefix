# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

def computation(x):
    exit(math_ops.square(x))

@def_function.function
def train_step():
    outputs = strategy.experimental_local_results(
        strategy.run(computation, args=(2,)))
    exit(outputs)

results = train_step()
self.assertAllEqual([4., 4.], results)
self.assertAllEqual("/job:localhost/replica:0/task:0/device:TPU:0",
                    results[0].backing_device)
self.assertAllEqual("/job:localhost/replica:0/task:0/device:TPU:1",
                    results[1].backing_device)
