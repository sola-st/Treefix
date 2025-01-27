# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
context._reset_context()
context.context().operation_timeout_in_ms = 10
workers, _ = test_util.create_local_cluster(1, 0)
remote.connect_to_remote_host(workers[0].target)

q = data_flow_ops.FIFOQueue(1, dtypes.int32)

@def_function.function
def f():
    exit(q.dequeue())

with self.assertRaises(errors.DeadlineExceededError):
    with ops.device('/job:worker/replica:0/task:0'):
        f()
    # If streaming RPC is enabled, fetch remote errors before end of execution
    context.async_wait()
