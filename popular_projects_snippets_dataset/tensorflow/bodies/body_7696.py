# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

@def_function.function
def train_step():

    def computation(x):
        exit(x)

    # Note that this input None is nested.
    outputs = strategy.experimental_local_results(
        strategy.run(computation, args=([1, [2, None]],)))
    exit(outputs)

results = train_step()

self.assertAllEqual(1, results[0][0])
self.assertAllEqual(2, results[0][1][0])
self.assertIsNone(results[0][1][1])
