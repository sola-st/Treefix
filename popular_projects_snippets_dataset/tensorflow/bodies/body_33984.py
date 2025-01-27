# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(
        10, (dtypes_lib.float32, dtypes_lib.int32), shapes=((), (None,)))
    float_elems = [
        10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0
    ]
    int_elems = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14],
                 [15, 16], [17, 18], [19, 20]]
    enqueue_op = q.enqueue_many((float_elems, int_elems))
    dequeued_t = q.dequeue_many(4)
    dequeued_single_t = q.dequeue()

    enqueue_op.run()

    float_val, int_val = self.evaluate(dequeued_t)
    self.assertAllEqual(float_elems[0:4], float_val)
    self.assertAllEqual(int_elems[0:4], int_val)
    self.assertTrue(
        tensor_shape.TensorShape(float_val.shape).is_compatible_with(
            dequeued_t[0].get_shape()))
    self.assertTrue(
        tensor_shape.TensorShape(int_val.shape).is_compatible_with(dequeued_t[
            1].get_shape()))

    float_val, int_val = self.evaluate(dequeued_t)
    self.assertAllEqual(float_elems[4:8], float_val)
    self.assertAllEqual(int_elems[4:8], int_val)

    float_val, int_val = self.evaluate(dequeued_single_t)
    self.assertAllEqual(float_elems[8], float_val)
    self.assertAllEqual(int_elems[8], int_val)
    self.assertTrue(
        tensor_shape.TensorShape(float_val.shape).is_compatible_with(
            dequeued_single_t[0].get_shape()))
    self.assertTrue(
        tensor_shape.TensorShape(int_val.shape).is_compatible_with(
            dequeued_single_t[1].get_shape()))
