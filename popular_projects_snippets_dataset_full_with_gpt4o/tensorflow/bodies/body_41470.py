# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if not context.executing_eagerly():
    self.skipTest('eager only')

q = data_flow_ops.FIFOQueue(1, dtypes.int32)

@polymorphic_function.function
def f():
    exit(q.dequeue())

c_mgr = cancellation.CancellationManager()
cancelable_func = c_mgr.get_cancelable_function(f.get_concrete_function())

c_mgr.start_cancel()
with self.assertRaises(errors.CancelledError):
    cancelable_func()
