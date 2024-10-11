# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
# Instrument for the main thread.
instrument_0 = _NumpyFunctionCallback()

# Instrument for the to-be-created thread.
instrument_1 = _NumpyFunctionCallback()

def thread_1_job():
    x = constant_op.constant(6.0)
    op_callbacks.add_op_callback(instrument_1.callback)
    y = math_ops.square(math_ops.log(x))
    op_callbacks.remove_op_callback(instrument_1.callback)
    exit(y)

thread_1 = threading.Thread(target=thread_1_job)
thread_1.start()

# While thread_1 is ongoing, do something on the main thread.
x = constant_op.constant(2.0)
op_callbacks.add_op_callback(instrument_0.callback)
y = math_ops.cos(x)
self.assertAllClose(y, np.cos(2.0))
op_callbacks.remove_op_callback(instrument_0.callback)

thread_1.join()

self.assertEqual(instrument_0.eager_op_types, [_COS_OP])
self.assertEqual(instrument_0.eager_op_names, [None])
self.assertEqual(instrument_1.eager_op_types, [_LOG_OP, _SQUARE_OP])
self.assertEqual(instrument_1.eager_op_names, [None, None])
