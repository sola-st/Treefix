# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
if context.num_gpus():
    self.skipTest("CPU-only test (requires unpartitioned graph).")

default_executor = test_util.TestDelta("flr_executor", "default")
single_threaded = test_util.TestDelta("flr_executor", "single_threaded")
run_async = test_util.TestDelta("pflr_runsync", "async")
run_sync = test_util.TestDelta("pflr_runsync", "sync")
safe = test_util.TestDelta("subgraph_async_summary", "safe_for_sync")

array_ops.fill([2], constant_op.constant(7, dtype=dtypes.int64))

assert default_executor.Get() == 0
assert single_threaded.Get() > 0
assert run_async.Get() == 0
assert run_sync.Get() > 0
assert safe.Get() > 0
