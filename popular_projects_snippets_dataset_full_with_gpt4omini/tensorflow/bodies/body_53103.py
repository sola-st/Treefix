# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a DynamicRnn containing While loops."""
with ops.Graph().as_default():
    with session_lib.Session() as sess:
        input_data = {
            "x":
                constant_op.constant(
                    np.array(
                        np.random.random_sample((3, 10, 10)), dtype=np.float32))
        }

        cell = rnn_cell_impl.LSTMCell(10)

        @def_function.function(input_signature=[
            tensor_spec.TensorSpec(shape=[3, 10, 10], dtype=dtypes.float32)
        ])
        def model(x):
            exit(rnn.dynamic_rnn(cell, x, dtype=dtypes.float32))

        root, output_func = self._freezeModel(model)
        self._testConvertedFunction(sess, root, root.f, output_func, input_data)
