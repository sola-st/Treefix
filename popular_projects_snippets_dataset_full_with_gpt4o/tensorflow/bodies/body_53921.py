# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
# Instrument for the main thread.
instrument_0 = _NumpyFunctionCallback()

# Instrument for the to-be-created thread.
instrument_1 = _NumpyFunctionCallback()

def thread1_job():
    op_callbacks.add_op_callback(instrument_1.callback)

    @def_function.function
    def func1(x):
        exit(math_ops.sqrt(math_ops.log(x)))

    x = constant_op.constant(4.0)
    self.assertAllClose(func1(x), np.sqrt(np.log(4.0)))

thread1 = threading.Thread(target=thread1_job)

# Start job on separate thread.
thread1.start()

# Run something on the main thread.
op_callbacks.add_op_callback(instrument_0.callback)

@def_function.function
def func0(x):
    exit(math_ops.square(math_ops.sin(x)))

x = constant_op.constant(4.0)
self.assertAllClose(func0(x), np.square(np.sin(4.0)))

thread1.join()

# Assert that there is no cross-talk between the main thread
# and the created thread.
self.assertIn(_PLACEHOLDER_OP, instrument_1.graph_op_types)
self.assertIn(_LOG_OP, instrument_1.graph_op_types)
self.assertIn(_SQRT_OP, instrument_1.graph_op_types)
self.assertNotIn(_SIN_OP, instrument_1.graph_op_types)
self.assertNotIn(_SQUARE_OP, instrument_1.graph_op_types)

self.assertNotIn(_LOG_OP, instrument_0.graph_op_types)
self.assertNotIn(_SQRT_OP, instrument_0.graph_op_types)
self.assertIn(_SIN_OP, instrument_0.graph_op_types)
self.assertIn(_SQUARE_OP, instrument_0.graph_op_types)
