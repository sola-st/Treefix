# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
if context.executing_eagerly():
    self.skipTest(
        "cross-device tests are not supported with eager execution.")
workers, _ = test_util.create_local_cluster(2, 0)
inputs = strategy.make_input_fn_iterator(
    lambda _: dataset_ops.Dataset.range(5))
comm_fn = lambda x: x + 1
run_op = strategy.experimental_run(comm_fn, inputs)
with session_lib.Session(target=workers[1].target) as sess:
    sess.run(inputs.initialize())
    sess.run(run_op)
