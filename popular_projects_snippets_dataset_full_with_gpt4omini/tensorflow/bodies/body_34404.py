# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with test_util.use_gpu():
    q = data_flow_ops.GPUCompatibleFIFOQueue(10, dtypes_lib.float32)
    elems_numpy = [10.0, 20.0, 30.0]
    # The identity ensures constants are copied to the GPU immediately
    elems = [array_ops.identity(constant_op.constant(x))
             for x in elems_numpy]

    for x in elems:
        self.evaluate(q.enqueue((x,)))

    for i in range(len(elems)):
        dequeued_tensor = q.dequeue()
        self.assertEqual(elems[0].device, dequeued_tensor.device)
        vals = self.evaluate(dequeued_tensor)
        self.assertEqual([elems_numpy[i]], vals)
