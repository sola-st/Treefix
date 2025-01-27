# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session() as sess:
    q = data_flow_ops.PaddingFIFOQueue(
        10, (dtypes_lib.string, dtypes_lib.int32),
        shapes=((None,), (1, None)))
    str_elems = [["a"], ["ab"], ["abc"], ["abc", "d"], ["abc", "d", "e"],
                 ["abc", "d", "e", "f"]]

    int_elems = [[[1]], [[2]], [[3]], [[1, 2]], [[1, 2, 3]], [[1, 2, 3, 4]]]

    enqueue_ops = [q.enqueue((str_elems[i], int_elems[i])) for i in range(6)]

    dequeued_t = q.dequeue_up_to(5)
    dequeued_single_t = q.dequeue()

    for enqueue_op in enqueue_ops:
        enqueue_op.run()
    string_val, int_val = self.evaluate(dequeued_t)

    self.assertAllEqual([[b"a", b"", b""], [b"ab", b"", b""],
                         [b"abc", b"", b""], [b"abc", b"d", b""],
                         [b"abc", b"d", b"e"]], string_val)
    self.assertAllEqual([[[1, 0, 0]], [[2, 0, 0]], [[3, 0, 0]], [[1, 2, 0]],
                         [[1, 2, 3]]], int_val)
    self.assertTrue(
        tensor_shape.TensorShape(string_val.shape).is_compatible_with(
            dequeued_t[0].get_shape()))
    self.assertTrue(
        tensor_shape.TensorShape(int_val.shape).is_compatible_with(dequeued_t[
            1].get_shape()))

    string_val, int_val = self.evaluate(dequeued_single_t)
    self.assertAllEqual([b"abc", b"d", b"e", b"f"], string_val)
    self.assertAllEqual([[1, 2, 3, 4]], int_val)
    self.assertTrue(
        tensor_shape.TensorShape(string_val.shape).is_compatible_with(
            dequeued_single_t[0].get_shape()))
    self.assertTrue(
        tensor_shape.TensorShape(int_val.shape).is_compatible_with(
            dequeued_single_t[1].get_shape()))
