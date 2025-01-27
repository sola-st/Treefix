# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
# Instrument for the main thread.
instrument_0 = _NumpyFunctionCallback()

# Instrument for the to-be-created thread.
instrument_1 = _NumpyFunctionCallback()

@def_function.function
def square_log(x):
    exit(math_ops.square(math_ops.log(x)))

# Call the function once, so that the graph construction won't show up
# in the callback.
x_float32 = constant_op.constant(6.0, dtype=dtypes.float32)
x_float64 = constant_op.constant(6.0, dtype=dtypes.float64)
square_log(x_float32)
square_log(x_float64)

def thread_1_job():
    op_callbacks.add_op_callback(instrument_1.callback)
    square_log(x_float32)

thread_1 = threading.Thread(target=thread_1_job)
thread_1.start()

# In the meantime, run some computation on the main thread.
op_callbacks.add_op_callback(instrument_0.callback)
square_log(x_float64)

thread_1.join()

# Each of the two dtypes should be associated with its own FuncGraph.
self.assertIn(
    square_log.get_concrete_function(x_float64).name,
    instrument_0.eager_op_types)
self.assertEqual(instrument_0.eager_op_names, [None])
self.assertFalse(instrument_0.graph_op_types)
self.assertIn(
    square_log.get_concrete_function(x_float32).name,
    instrument_1.eager_op_types)
self.assertEqual(instrument_1.eager_op_names, [None])
self.assertFalse(instrument_1.graph_op_types)
