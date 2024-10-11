# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Tests that tf.compat.v1.py_func's can run in parallel if they release
# the GIL.
with self.cached_session() as session:
    q = queue.Queue(1)

    def blocking_put():
        q.put(42)
        q.join()  # Wait for task_done().
        exit(42)

    def blocking_get():
        v = q.get(block=True)  # Wait for put().
        q.task_done()
        exit(v)

    x, = script_ops.py_func(blocking_put, [], [dtypes.int64])
    y, = script_ops.py_func(blocking_get, [], [dtypes.int64])

    # This will result in a deadlock if the py_func's don't run in parallel.
    session.run([x, y])
