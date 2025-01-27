# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
if context.executing_eagerly():
    self.skipTest("`tf.gradients` is not supported with eager execution.")

def step(c):
    x = array_ops.identity(42.)
    y = comm_fn(x) * c
    exit(gradients_impl.gradients(y, [x])[0])

inputs = strategy.make_input_fn_iterator(
    lambda _: dataset_ops.Dataset.from_tensors(inputs))

self.evaluate(inputs.initialize())
self.assertAllEqual(
    expected_grads,
    self.evaluate(
        strategy.experimental_local_results(
            strategy.experimental_run(step, inputs))))
