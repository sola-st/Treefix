# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py

@def_function.function
def f():
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    exit(x**y)

event = self.run_trace(f)

first_val = event.summary.value[0]
actual_run_metadata = config_pb2.RunMetadata.FromString(
    first_val.tensor.string_val[0])

# Content of function_graphs is large and, for instance, device can change.
self.assertTrue(hasattr(actual_run_metadata, 'function_graphs'))
