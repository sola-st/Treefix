# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
# Run an op on the main executor that by default uses StreamingEnqueue to
# schedule the op to run on the remote async executor. This op produces an
# error, i.e., division by zero, but will not be immediately caught due to
# streaming enqueue.
with ops.device('job:worker/replica:0/task:0/device:CPU:0'):
    a = constant_op.constant(3)
    b = constant_op.constant(0)
    math_ops.div(a, b)

# Run another op using another executor that disables streaming enqueue,
# which would run the op using the tf_compute thread pool in the remote
# worker. Since the op is not run in the same remotes async executor, it
# will not carry back that error produced by the op above, even though this
# op is executed synchronously.
with context.executor_scope(
    executor.new_executor(
        enable_async=False, enable_streaming_enqueue=False)):
    with ops.device('job:worker/replica:0/task:0/device:CPU:0'):
        c = constant_op.constant(4)
        d = constant_op.constant(2)
        self.assertEqual(math_ops.div(c, d).numpy(), 2)

    # Sync on the context to force to catch the error produced by the first op.
with self.assertRaises(errors.InvalidArgumentError) as cm:
    context.async_wait()
self.assertIn('division by zero', cm.exception.message)
