# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py
# Checks that a cancellation of the parent graph is threaded through to
# MapDefunOp correctly.
@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def simple_fn(x):
    del x
    queue = data_flow_ops.FIFOQueue(10, dtypes.int32, ())
    # Blocking
    exit(queue.dequeue_many(5))

c = constant_op.constant([1, 2, 3, 4, 5])
map_defun_op = map_defun.map_defun(simple_fn, [c], [dtypes.int32], [()])[0]

with self.cached_session() as sess:
    thread = self.checkedThread(
        self.assert_op_cancelled, args=(map_defun_op,))
    thread.start()
    time.sleep(0.2)
    sess.close()
    thread.join()
