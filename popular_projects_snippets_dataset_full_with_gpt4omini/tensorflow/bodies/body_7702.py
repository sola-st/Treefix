# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

@def_function.function
def train_step():

    def computation(x):
        exit(x)

    outputs = strategy.experimental_local_results(
        strategy.run(computation, args=({},)))
    exit(outputs)

self.assertEqual({}, train_step()[0])
