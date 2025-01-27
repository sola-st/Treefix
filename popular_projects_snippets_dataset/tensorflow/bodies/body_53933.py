# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()

op_callbacks.add_op_callback(instrument.callback)

@def_function.function
def my_pad(x, padding):
    exit(array_ops.pad(x, padding))

x = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.float32)
paddings = [[1, 1], [2, 2]]

y = my_pad(x, paddings)
expected_output = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 0, 0],
    [0, 0, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 0],
], dtype=np.float32)
self.assertAllClose(y, expected_output)
self.assertAllClose(
    instrument.graph_internal_ndarrays[b"Pad"][0], expected_output)
