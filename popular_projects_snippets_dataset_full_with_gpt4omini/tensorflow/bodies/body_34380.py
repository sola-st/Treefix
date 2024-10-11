# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py

class _M(module.Module):

    def __init__(self):
        self.q1 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
        self.q2 = None

    @def_function.function
    def uses_queues(self, x):
        if self.q2 is None:
            self.q2 = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
        self.q2.enqueue(x)
        self.q2.enqueue(x + 3)
        self.q1.enqueue(self.q2.dequeue())

m = _M()
self.evaluate(m.uses_queues(constant_op.constant(2)))
self.assertAllEqual(2, self.evaluate(m.q1.dequeue()))
self.assertAllEqual(5, self.evaluate(m.q2.dequeue()))
if context.executing_eagerly():
    q1_handle = m.q1.queue_ref
    q2_handle = m.q2.queue_ref
    del m
    gc.collect()
    # If executing eagerly, deleting the Module should clean up the queue
    # resources.
    with self.assertRaisesRegex(errors_impl.NotFoundError,
                                r"Resource .* does not exist."):
        gen_resource_variable_ops.destroy_resource_op(
            q1_handle, ignore_lookup_error=False)
    with self.assertRaisesRegex(errors_impl.NotFoundError,
                                r"Resource .* does not exist."):
        gen_resource_variable_ops.destroy_resource_op(
            q2_handle, ignore_lookup_error=False)
