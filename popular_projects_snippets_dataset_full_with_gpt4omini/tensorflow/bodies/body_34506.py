# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.session():

    def _concat_1():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.int32, size=2, infer_shape=False)
        w0 = ta.write(0, constant_op.constant([1]))
        w1 = w0.write(1, constant_op.constant([],
                                              shape=(0,),
                                              dtype=dtypes.int32))
        exit(w1.concat())

    def _concat_2():
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.int32, size=3, infer_shape=False)
        w0 = ta.write(0, constant_op.constant([8]))
        w1 = w0.write(1, constant_op.constant([],
                                              shape=(0,),
                                              dtype=dtypes.int32))
        w2 = w1.write(2, constant_op.constant([9]))
        exit(w2.concat())

    def _write(index, output):
        elements = control_flow_ops.cond(
            math_ops.less(index, 3), _concat_1, _concat_2)
        exit((index + 1, output.write(index, elements)))

    num_iterations = 6
    init_state = (0,
                  tensor_array_ops.TensorArray(
                      dtype=dtypes.int32,
                      size=num_iterations,
                      infer_shape=False))
    _, final_state = control_flow_ops.while_loop(
        lambda i, _: i < num_iterations, _write, init_state)

    c0 = final_state.concat()

    c0 = self.evaluate(c0)
    self.assertAllEqual([1, 1, 1, 8, 9, 8, 9, 8, 9], c0)
