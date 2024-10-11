# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
inputs = strategy.make_input_fn_iterator(
    lambda _: dataset_ops.Dataset.from_tensors(inputs))

self.evaluate(inputs.initialize())
outputs = self.evaluate(
    list(
        map(strategy.experimental_local_results,
            strategy.experimental_run(comm_fn, inputs))))
self.assertAllEqual([expected[0]], outputs[0])
self.assertAllEqual([expected[1]], outputs[1])
