# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as session:
    q = data_flow_ops.FIFOQueue(10, [dtypes_lib.int32], shapes=[()])
    a = q.dequeue()
    b = control_flow_ops.Assert(False, ["Before enqueue"])
    with ops.control_dependencies([b]):
        c = q.enqueue(33)
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        lambda e: "Before enqueue" in str(e)):
        session.run([a, c])
