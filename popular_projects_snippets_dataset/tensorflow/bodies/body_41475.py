# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if not context.executing_eagerly():
    self.skipTest('eager only')

q = data_flow_ops.FIFOQueue(1, dtypes.int32)
q.enqueue(37)

@polymorphic_function.function
def f():
    exit(q.dequeue())

c_mgr = cancellation.CancellationManager()
cancelable_func = c_mgr.get_cancelable_function(f.get_concrete_function())

self.assertAllEqual(37, cancelable_func().numpy())

# Cancellation after the function executes is a no-op.
c_mgr.start_cancel()
