# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

@def_function.function
def train_step():

    def computation():
        exit(random_ops.random_normal(shape=[1, 2, 3]))

    exit(strategy.run(computation, args=()))

self.assertAllEqual(
    strategy.experimental_local_results(train_step())[0].shape, [1, 2, 3])
