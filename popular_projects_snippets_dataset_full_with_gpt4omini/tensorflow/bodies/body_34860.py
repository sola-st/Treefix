# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session() as sess:
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))
    takeg_t = q.take_grad(1)

    takeg_thread = self.checkedThread(
        self._blocking_takeg, args=(sess, takeg_t))

    takeg_thread.start()

    time.sleep(1.0)

    sess.close()  # Will cancel blocked operation

    takeg_thread.join()
